import numpy as np
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener


def matriz_se3(t, q):
    x, y, z, w = q.x, q.y, q.z, q.w
    R = np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [t.x, t.y, t.z]
    return T


class BaseToolTF(Node):
    def __init__(self):
        super().__init__('base_tool_tf')
        self.buffer = Buffer()
        self.listener = TransformListener(self.buffer, self)
        self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        try:
            tf = self.buffer.lookup_transform('base_link', 'tool0', rclpy.time.Time())
        except TransformException as ex:
            self.get_logger().warn(f'Esperando TF base_link -> tool0: {ex}')
            return
        T = matriz_se3(tf.transform.translation, tf.transform.rotation)
        np.set_printoptions(precision=4, suppress=True)
        self.get_logger().info(f'base_link -> tool0 (SE3):\n{T}')


def main():
    rclpy.init()
    node = BaseToolTF()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()

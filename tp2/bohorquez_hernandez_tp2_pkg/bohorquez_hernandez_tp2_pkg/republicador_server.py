import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from bohorquez_hernandez_interfaces.action import Republicar


class RepublicadorServer(Node):
    def __init__(self):
        super().__init__('nodo1')
        ActionServer(self, Republicar, 'republicar', self.ejecutar)

    def ejecutar(self, goal_handle):
        texto = goal_handle.request.texto
        self.get_logger().info(f'Republicando: {texto}')
        fb = Republicar.Feedback()
        for palabra in texto.split():
            fb.palabra = palabra
            goal_handle.publish_feedback(fb)
            time.sleep(1.0)
        goal_handle.succeed()
        return Republicar.Result(resultado='Texto republicado!')


def main():
    rclpy.init()
    rclpy.spin(RepublicadorServer())
    rclpy.shutdown()


if __name__ == '__main__':
    main()

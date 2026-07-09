import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from bohorquez_hernandez_interfaces.srv import ResetContador


class Monitor(Node):
    def __init__(self):
        super().__init__('monitor')
        self.declare_parameter('valor_reset', 0)
        self.declare_parameter('umbral', 50)
        self.valor_reset = self.get_parameter('valor_reset').value
        self.umbral = self.get_parameter('umbral').value

        self.cli = self.create_client(ResetContador, 'reset_contador')
        self.create_subscription(Int32, 'contador', self.callback, 10)
        self.esperando = False

    def callback(self, msg):
        if msg.data >= self.umbral and not self.esperando and self.cli.service_is_ready():
            self.esperando = True
            self.get_logger().info(f'llego a {msg.data}, pido reset')
            req = ResetContador.Request(valor=self.valor_reset)
            self.cli.call_async(req).add_done_callback(self.listo)

    def listo(self, future):
        self.esperando = False


def main():
    rclpy.init()
    rclpy.spin(Monitor())
    rclpy.shutdown()


if __name__ == '__main__':
    main()

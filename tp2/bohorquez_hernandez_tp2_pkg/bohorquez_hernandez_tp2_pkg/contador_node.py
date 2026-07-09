import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from bohorquez_hernandez_interfaces.srv import ResetContador


class Contador(Node):
    def __init__(self):
        super().__init__('contador')
        self.declare_parameter('frecuencia', 5.0)
        self.declare_parameter('max_cuenta', 1000)
        self.frecuencia = self.get_parameter('frecuencia').value
        self.max_cuenta = self.get_parameter('max_cuenta').value

        self.cuenta = 0
        self.pub = self.create_publisher(Int32, 'contador', 10)
        self.create_timer(1.0 / self.frecuencia, self.tick)
        self.create_service(ResetContador, 'reset_contador', self.reset)

    def tick(self):
        self.pub.publish(Int32(data=self.cuenta))
        self.get_logger().info(f'contador: {self.cuenta}')
        if self.cuenta < self.max_cuenta:
            self.cuenta += 1

    def reset(self, request, response):
        self.cuenta = request.valor
        self.get_logger().info(f'contador reseteado a {request.valor}')
        response.ok = True
        return response


def main():
    rclpy.init()
    rclpy.spin(Contador())
    rclpy.shutdown()


if __name__ == '__main__':
    main()

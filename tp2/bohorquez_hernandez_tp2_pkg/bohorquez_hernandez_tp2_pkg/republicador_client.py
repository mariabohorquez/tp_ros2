import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from bohorquez_hernandez_interfaces.action import Republicar

TEXTO_DEFAULT = 'You must gather your party before venturing forth'


class RepublicadorClient(Node):
    def __init__(self):
        super().__init__('nodo2')
        self.declare_parameter('texto', TEXTO_DEFAULT)
        self.texto = self.get_parameter('texto').value
        self.cli = ActionClient(self, Republicar, 'republicar')

    def enviar(self):
        self.cli.wait_for_server()
        goal = Republicar.Goal(texto=self.texto)
        fut = self.cli.send_goal_async(goal, feedback_callback=self.feedback)
        fut.add_done_callback(self.aceptado)

    def feedback(self, msg):
        self.get_logger().info(msg.feedback.palabra)

    def aceptado(self, future):
        future.result().get_result_async().add_done_callback(self.resultado)

    def resultado(self, future):
        self.get_logger().info(future.result().result.resultado)
        rclpy.shutdown()


def main():
    rclpy.init()
    nodo = RepublicadorClient()
    nodo.enviar()
    rclpy.spin(nodo)


if __name__ == '__main__':
    main()

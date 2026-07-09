from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    texto = LaunchConfiguration('texto')
    return LaunchDescription([
        DeclareLaunchArgument(
            'texto',
            default_value='You must gather your party before venturing forth',
        ),
        Node(
            package='bohorquez_hernandez_tp2_pkg', executable='republicador_server',
            name='nodo1',
        ),
        Node(
            package='bohorquez_hernandez_tp2_pkg', executable='republicador_client',
            name='nodo2',
            parameters=[{'texto': ParameterValue(texto, value_type=str)}],
        ),
    ])

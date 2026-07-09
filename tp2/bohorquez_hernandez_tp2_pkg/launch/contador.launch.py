from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    frecuencia = LaunchConfiguration('frecuencia')
    valor_reset = LaunchConfiguration('valor_reset')
    umbral = LaunchConfiguration('umbral')
    return LaunchDescription([
        DeclareLaunchArgument('frecuencia', default_value='5.0'),
        DeclareLaunchArgument('valor_reset', default_value='0'),
        DeclareLaunchArgument('umbral', default_value='50'),
        Node(
            package='bohorquez_hernandez_tp2_pkg', executable='contador', name='contador',
            parameters=[{'frecuencia': ParameterValue(frecuencia, value_type=float)}],
        ),
        Node(
            package='bohorquez_hernandez_tp2_pkg', executable='monitor', name='monitor',
            parameters=[
                {'valor_reset': ParameterValue(valor_reset, value_type=int)},
                {'umbral': ParameterValue(umbral, value_type=int)},
            ],
        ),
    ])

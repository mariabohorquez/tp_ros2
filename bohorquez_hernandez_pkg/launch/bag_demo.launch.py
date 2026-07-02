import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    default_bag_path = os.path.join(
        os.path.expanduser('~'), 'tp_ros2_bags', 'running')

    bag_path_arg = DeclareLaunchArgument(
        name='bag_path',
        default_value=default_bag_path,
        description='Carpeta del rosbag ROS 2 (Unitree Go1 - Leg-KILO, secuencia running)')
    bag_path = LaunchConfiguration('bag_path')

    pkg_share = get_package_share_directory('bohorquez_hernandez_pkg')
    rviz_config = os.path.join(pkg_share, 'rviz', 'go1_running.rviz')
    rqt_perspective = os.path.join(pkg_share, 'config', 'topics_perspective.perspective')

    # Reproduce el rosbag en loop, publicando /clock para que RViz pueda
    # usar el tiempo simulado de la grabacion en vez del reloj de pared.
    bag_play = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', bag_path, '--clock', '--loop'],
        output='screen')

    # El bag no incluye /tf. Publicamos una transformada estatica identidad
    # entre el frame del LiDAR (velodyne) y el de la odometria (sdk_odom)
    # para que RViz pueda mostrar ambos en un mismo Fixed Frame; no contamos
    # con la calibracion real entre sensores del Go1, asi que es aproximada.
    static_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='velodyne_to_sdk_odom',
        arguments=['0', '0', '0', '0', '0', '0', 'velodyne', 'sdk_odom'],
        parameters=[{'use_sim_time': True}])

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        parameters=[{'use_sim_time': True}],
        output='screen')

    rqt_node = Node(
        package='rqt_gui',
        executable='rqt_gui',
        name='rqt_gui',
        arguments=['--perspective-file', rqt_perspective],
        output='screen')

    return LaunchDescription([
        bag_path_arg,
        LogInfo(msg=['Reproduciendo rosbag desde: ', bag_path]),
        bag_play,
        static_tf_node,
        rviz_node,
        rqt_node,
    ])

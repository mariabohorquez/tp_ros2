import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    dp_launch = os.path.join(
        get_package_share_directory('clase3'), 'launch', 'dp_launch.py')
    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource(dp_launch)),
        Node(
            package='bohorquez_durante_tp3_pkg',
            executable='base_tool_tf',
            name='base_tool_tf',
        ),
    ])

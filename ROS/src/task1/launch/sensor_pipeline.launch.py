from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='task1', executable='sensor', name='sensor', output='screen'),
        Node(package='task1', executable='processor', name='processor', output='screen'),
        Node(package='task1', executable='logger', name='logger', output='screen'),
    ])

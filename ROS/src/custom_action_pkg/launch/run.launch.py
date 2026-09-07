from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='custom_action_pkg', executable='server', name='action_server', output='screen'),
        Node(package='custom_action_pkg', executable='client', name='action_client', output='screen'),
    ])

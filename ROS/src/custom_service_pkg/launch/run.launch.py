from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='custom_service_pkg', executable='server', name='server', output='screen'),
        Node(package='custom_service_pkg', executable='client', name='client', output='screen'),
    ])

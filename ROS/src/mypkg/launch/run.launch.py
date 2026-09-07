from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(package='mypkg', executable='pub', name='pub', output='screen', emulate_tty=True),
        Node(package='mypkg', executable='sub', name='sub', output='screen', emulate_tty=True),
    ])

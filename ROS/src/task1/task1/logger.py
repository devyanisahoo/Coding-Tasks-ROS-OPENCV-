import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
class Logger(Node):
    def __init__(self):
        super().__init__('logger')
        self.sub = self.create_subscription(Vector3, '/processeddata', self.callback, 10)
    def callback(self, msg):
        self.get_logger().info(f'Log: {msg.x:.2f}')
def main():
    rclpy.init()
    node = Logger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

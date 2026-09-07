import rclpy
from rclpy.node import Node
from msgpkg.msg import Status
class Sub(Node):
    def __init__(self):
        super().__init__('sub')
        self.s = self.create_subscription(Status, '/stat', self.callback, 10)
    def callback(self, msg):
        self.get_logger().info(f'Name: {msg.name} | Batt: {msg.batt}% | Move: {msg.move} | Err: {msg.err}')
def main():
    rclpy.init()
    node = Sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

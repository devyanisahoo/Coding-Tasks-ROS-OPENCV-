import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
import math
class Processor(Node):
    def __init__(self):
        super().__init__('processor')
        self.sub = self.create_subscription(Vector3, '/sensordata', self.callback, 10)
        self.pub = self.create_publisher(Vector3, '/processeddata', 10)
    def callback(self, msg):
        length = math.sqrt(msg.x**2 + msg.y**2 + msg.z**2)
        self.pub.publish(Vector3(x=length, y=0.0, z=0.0))
        self.get_logger().info(f'Length: {length:.2f}')
def main():
    rclpy.init()
    node = Processor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

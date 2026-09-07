import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')
        self.declare_parameter('rate', 2.0)
        self.pub = self.create_publisher(Vector3, '/sensordata', 10)
        self.timer = self.create_timer(0.5, self.publish_data)
        self.cnt = 1
    def publish_data(self):
        hz = float(self.get_parameter('rate').value)
        if self.timer.timer_period_ns != int(1e9 / hz):
            self.timer.timer_period_ns = int(1e9 / hz)
        msg = Vector3()
        msg.x = float(self.cnt)
        msg.y = float(self.cnt + 1)
        msg.z = float(self.cnt + 2)
        self.pub.publish(msg)
        self.get_logger().info(f'Sent: {msg.x}, {msg.y}, {msg.z} ({hz}Hz)')
        self.cnt += 1
        if self.cnt > 100:
            self.cnt = 1
def main():
    rclpy.init()
    node = Sensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

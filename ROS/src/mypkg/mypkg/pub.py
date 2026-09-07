import rclpy
from rclpy.node import Node
from msgpkg.msg import Status
class Pub(Node):
    def __init__(self):
        super().__init__('pub')
        self.declare_parameter('rate',1.0)
        self.p=self.create_publisher(Status,'/stat',10)
        self.timer=self.create_timer(1.0,self.publishdata)
        self.batt=100.0
    def publishdata(self):
        hz = float(self.get_parameter('rate').value)
        self.timer.timer_period_ns = int(1e9 / hz)
        msg = Status()
        msg.name = 'bot1'
        msg.batt = self.batt
        msg.move = True
        msg.err = 0
        self.p.publish(msg)
        self.get_logger().info(f'Sent: {msg.name} ({hz}Hz)')
        self.batt = round(max(0.0, self.batt - 0.5), 1)
def main():
    rclpy.init()
    node = Pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

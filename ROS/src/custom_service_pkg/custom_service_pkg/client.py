import rclpy
from rclpy.node import Node
from msgpkg.srv import AddTwoInts
class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.cli = self.create_client(AddTwoInts, '/add')
        self.timer = self.create_timer(2.0, self.send)
    def send(self):
        if not self.cli.service_is_ready():
            self.get_logger().info('waiting')
            return
        req = AddTwoInts.Request()
        req.a = 3
        req.b = 7
        future = self.cli.call_async(req)
        future.add_done_callback(self.done)
    def done(self, future):
        res = future.result()
        self.get_logger().info(f'sum: {res.sum}')
def main():
    rclpy.init()
    node = Client()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

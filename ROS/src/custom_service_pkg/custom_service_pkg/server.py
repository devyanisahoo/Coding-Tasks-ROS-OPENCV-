import rclpy
from rclpy.node import Node
from msgpkg.srv import AddTwoInts
class Server(Node):
    def __init__(self):
        super().__init__('server')
        self.srv = self.create_service(AddTwoInts, '/add', self.add)
        self.get_logger().info('ready')
    def add(self, req, res):
        res.sum = req.a + req.b
        self.get_logger().info(f'{req.a} + {req.b} = {res.sum}')
        return res
def main():
    rclpy.init()
    node = Server()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

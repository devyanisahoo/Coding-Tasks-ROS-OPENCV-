import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from msgpkg.action import CountDown

class Server(Node):
    def __init__(self):
        super().__init__('action_server')
        self._action_server = ActionServer(
            self,
            CountDown,
            'countdown',
            self.execute_callback)
    def execute_callback(self, goal_handle):
        target = goal_handle.request.target
        self.get_logger().info(f'Received goal to count down from: {target}')
        feedback_msg = CountDown.Feedback()
        count = target
        while count >= 0:
            feedback_msg.current_count = count
            self.get_logger().info(f'Publishing feedback: {count}')
            goal_handle.publish_feedback(feedback_msg)
            count -= 1
            time.sleep(1.0)
        goal_handle.succeed()
        result = CountDown.Result()
        result.status = 'Done!'
        self.get_logger().info('Goal succeeded.')
        return result

def main(args=None):
    rclpy.init(args=args)
    node = Server()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

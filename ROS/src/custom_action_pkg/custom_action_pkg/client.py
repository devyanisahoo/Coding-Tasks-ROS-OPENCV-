import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from msgpkg.action import CountDown

class Client(Node):
    def __init__(self):
        super().__init__('action_client')
        self._action_client = ActionClient(self, CountDown, 'countdown')
        self.send_goal(10)
    def send_goal(self, target):
        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()

        goal_msg = CountDown.Goal()
        goal_msg.target = target

        self.get_logger().info(f'Sending goal: {target}')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            return
        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'[FEEDBACK] Remaining: {feedback_msg.feedback.current_count}')
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'[RESULT] Server response: {result.status}')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = Client()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

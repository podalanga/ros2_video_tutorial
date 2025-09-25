import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci') #the  "_" is just a convention to prevent confusion

    def send_goal(self, order):
        goal_msg=Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()
        
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    
    def goal_response_callback(self,future):
        goal_handle=future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected: saavu da")
            return
        self.get_logger().info("Goal accepted Nice...")
        self._get_result_future=goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    

def main(args=None):
    rclpy.init(args=args)
    action_client=FibonacciActionClient()
    future=action_client.send_goal(10)
    rclpy.spin_until_future_complete(action_client,future)

if __name__=="__main__":
    main()

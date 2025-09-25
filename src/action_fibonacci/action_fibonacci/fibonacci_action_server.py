import rclpy
from rclpy. action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci

class FibonacciActionServ(Node):
    def __init__(self):
        super().__init__("josh_fibonacci")
        self.action_server=ActionServer(self, Fibonacci,'fibonacci',self.execute_callback)
    
    def execute_callback(self, goal_handle):
        self.get_logger().info("Executing.....")
        sequence =[0,1]
        for i in range(1,goal_handle.request.order):
            sequence.append(sequence[i]+sequence[i-1])
        goal_handle.fail() #this is a function which tells you if it got succeeded in completeing the action
        result=Fibonacci.Result()
        result.sequence=sequence
        return result

def main (args=None):
    rclpy.init(args=args)

    fibonacci_action_serv=FibonacciActionServ()
    rclpy.spin(fibonacci_action_serv)

if __name__ =="__main__":
    main()

'''
here is the output of ros2 action  list -t

/fibonacci [action_tutorials_interfaces/action/Fibonacci]
'''

#command: ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"


'''
Output:

Waiting for an action server to become available...
Sending goal:
     order: 5

Goal accepted with ID: 523135b3dc584f2d8c014678daa2e2ff

Result:
    sequence:
- 0
- 1
- 1
- 2
- 3
- 5

Goal finished with status: SUCCEEDED
'''

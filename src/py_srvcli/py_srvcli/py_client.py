import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys


class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__("minimal_client_async")
        self.client=self.create_client(AddTwoInts,'add_two_ints') #note the 'add_two_ints'. this should match with the service and client else no communication
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, wait panren")
        self.req=AddTwoInts.Request()
    def send_request(self,a,b):
        self.req.a=a
        self.req.b=b
        return self.client.call_async(self.req)
def main(args=None):
    rclpy.init(args=args)

    minimal_client =MinimalClientAsync()
    #we need the client to wait for the future object to come from server
    future=minimal_client.send_request(int(sys.argv[1]),int(sys.argv[2])) #argument sent from terminal. argv[0] gives the program/script name which we dont need.
    rclpy.spin_until_future_complete(minimal_client,future)
    response=future.result()
    minimal_client.get_logger().info(
        f"result of manual: {sys.argv[1]} + {sys.argv[2]} \n result of server response: {response.sum}"
    )
    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__== "__main__":
    main()

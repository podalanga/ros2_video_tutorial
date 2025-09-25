import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class minimal_service_josh(Node):
    def __init__(self):
        super().__init__("john_doe")
        self.srv=self.create_service(AddTwoInts,'add_two_ints',self.add_two_int_callback)

    def add_two_int_callback(self, request, response):
        response.sum=request.a+request.b
        self.get_logger().info("incoming request\na: %d and b: %d" %(request.a,request.b))

        return response

def main(args=None):
    rclpy.init(args=args)
    example_service=minimal_service_josh()
    rclpy.spin(example_service)
    example_service.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
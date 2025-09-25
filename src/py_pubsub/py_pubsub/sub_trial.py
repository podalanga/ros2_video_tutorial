import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MininalSubscriber(Node):
    def __init__(self):
        super().__init__("josh_sub")
        self.subscriber_=self.create_subscription(String,'topic1',self.listener_callback,10)

    def listener_callback(self,msg):
        self.get_logger().info("Sunnaya: %s" % msg.data)

def main(args=None):
    rclpy.init(args=args)
    sub1=MininalSubscriber()
    rclpy.spin(sub1)
    
    sub1.destroy_node()
    rclpy.shutdown

if __name__=="__main__":
    main()
import rclpy #ros client library
from rclpy.node import Node
from std_msgs.msg import String #these are standard ros messages not the typical String which you see in python

class MinialPublisher(Node): #inheritance. parent class is Node
    def __init__(self):
        super().__init__("josh_pub") #refer the Node, it needs a unique string to identify. super().__init__ for calling the constructor of parent
        self.publisher_=self.create_publisher(String,'topic1',10) #the 10 is the queue size
        # the underscore is used to prevent any name clashes. This is a naming convention for instances in ros2
        timer_period=0.5 #seconds
        self.timer=self.create_timer(timer_period,self.timer_callback)
        self.i=0

    def timer_callback(self):
        msg=String() #mind you this in not a python string, this is a interface format of ros2 message
        msg.data='Poda punnaku: %d' %self.i
        self.publisher_.publish(msg)
        self.get_logger().info('News laundry: %s' % msg.data)
        self.i+=1
        

def main(args=None):
    rclpy.init(args=args) #ros client init
    pub1=MinialPublisher() #class init

    #if this is run, it will run for only once. we need it to publish indefinitely
    rclpy.spin(pub1) #spin makes it indefinite
    
    #we dont need to destroy the spin explicitly. Python has a garbage collector which automatically takes care of it
    #But it is a good habit to destroy it manually

    pub1.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
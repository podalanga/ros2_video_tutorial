import rclpy
from rclpy.node import Node

class MinimalParam(Node):
    def __init__(self):
        super().__init__("param_basics_node")
        
        from rcl_interfaces.msg import ParameterDescriptor
        #my_parameter_descriptor = ParameterDescriptor(description='This parameter is mine!')
        #self.declare_parameter("param_basics","hello",my_parameter_descriptor)
        self.declare_parameter("param_basics","hellowww")
        self.timer=self.create_timer(1,self.timer_callback)
        self.some_cond=1

    def timer_callback(self):
        my_param=self.get_parameter("param_basics").get_parameter_value().string_value
        self.get_logger().info(f"say Hello from param server {my_param}")
        
        if self.some_cond:

            my_new_param=rclpy.parameter.Parameter('param_basics',rclpy.Parameter.Type.STRING,'hello2')

            all_new_parameters=[my_new_param]
            self.set_parameters(all_new_parameters)
        
        #Note the param_basics should remain same for that specific parameter
        
        '''

        here it is an array
        useful in the cases of batch update 
        new_params = [
            rclpy.parameter.Parameter('robot_speed', rclpy.Parameter.Type.DOUBLE, 2.5),
            rclpy.parameter.Parameter('robot_direction', rclpy.Parameter.Type.STRING, 'forward'),
            rclpy.parameter.Parameter('safety_mode', rclpy.Parameter.Type.BOOL, True)
        ]
        self.set_parameters(new_params) 
        '''

        '''
        to update the param, here is the way
        ros2 param set /minimal_param_node my_parameter "ROS2"
        '''
def main():
    rclpy.init()
    node=MinimalParam()
    rclpy.spin(node)

if __name__=="__main__":
    main()
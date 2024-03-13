import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import String

class SensorDataPublisher(Node):
    def __init__(self):
        super().__init__('sensor_data_publisher')
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        sensor_data = random.randint(0, 100)
        msg.data = str(sensor_data)
        self.publisher_.publish(msg)
        self.get_logger().info('distance from wall: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    sensor_data_publisher = SensorDataPublisher()
    rclpy.spin(sensor_data_publisher)
    sensor_data_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

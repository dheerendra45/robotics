
import rclpy
import random
from rclpy.node import Node

from std_msgs.msg import String


class sensordata(Node):

    def __init__(self):
        super().__init__('sensordata')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        sensordata = random.randint(1, 10000)
        msg.data = 'sensor data %d %d' % (sensordata, self.i)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1



def main(args=None):
    rclpy.init(args=args)

    sensor_data= sensordata()

    rclpy.spin(sensor_data)
    sensor_data.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

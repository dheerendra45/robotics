import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SensorDataSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_data_subscriber')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        sensor_data = int(msg.data)
        if sensor_data >= 80:
            self.get_logger().info('Warning: Sensor data value exceeds 80')
        else:
            self.get_logger().info('Safe: Sensor data value is %d' % sensor_data)

def main(args=None):
    rclpy.init(args=args)
    sensor_data_subscriber = SensorDataSubscriber()
    rclpy.spin(sensor_data_subscriber)
    sensor_data_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

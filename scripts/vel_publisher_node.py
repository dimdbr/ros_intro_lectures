#!/usr/bin/env python3 

# import the ros libraries to this node
import rospy
# import geomentry_msg Twist from ROS libraries 
from geometry_msgs.msg import Twist 

if __name__ == '__main__': 
	# define a publisher to velocity send commands (topic, msg type, queue size)
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# init the node (file name)
	rospy.init_node('vel_publisher_node',anonymous = True)
	# create a loop rate (timer)
	# set freuquency rate at 10 Hz
	loop_rate = rospy.Rate(10)
	# create msg for sending comments 
	vel_cmd = Twist()
	# setup ctrl loop 
	while not rospy.is_shutdown(): 
		# set linear vel
		vel_cmd.linear.x = 1.0
		# set angular vel 
		vel_cmd.angular.z = 0.5 
		# publish msg 
		cmd_pub.publish(vel_cmd)  
		# sleep for next iter 
		loop_rate.sleep() 

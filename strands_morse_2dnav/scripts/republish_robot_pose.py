#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped

class PoseRepublisher():
	"A class to republish pose information"

	def __init__(self):
		rospy.init_node('pose_republisher')
		self.pub = rospy.Publisher('/robot_pose', Pose) 
		rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, self.callback) 
		rospy.logdebug(rospy.get_name() + " setting up")

	def callback(self,pose): 
		rospy.logdebug(rospy.get_name() + ": I heard %s" % pose)
		self.pub.publish(pose.pose.pose)

if __name__ == '__main__':
    republisher = PoseRepublisher()
    rospy.spin()
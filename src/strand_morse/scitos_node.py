#! /usr/bin/env python
import roslib; roslib.load_manifest('strands_morse')
import rospy

# messages
from scitos_msgs.msg import MotorStatus

# services
from scitos_msgs.srv import EmergencyStop
from scitos_msgs.srv import EnableMotors
from scitos_msgs.srv import ResetOdometry
from scitos_msgs.srv import ResetMotorStop


def emergency_stop():
    return EmergencyStopResponce()

def enable_motors():
    return EnableMotorsResponce()

def reset_odometry():
    return ResetOdometryResponce()

def reset_motorstop():
    return ResetMotorStopResponce()
        
if __name__ == '__main__':


    try:
        rospy.init_node('scitos_node')
        rospy.loginfo("Starting fake scitos_node")
        s1 = rospy.Service('emergency_stop', EmergencyStop, emergency_stop)
        s2 = rospy.Service('enable_motors',  EnableMotors,  enable_motors)
        s3 = rospy.Service('reset_odometry', ResetOdometry, reset_odometry)
        s4 = rospy.Service('reset_motorstop',ResetMotorStop,reset_motorstop)

        pub = rospy.Publisher('motor_status', MotorStatus)
        while not rospy.is_shutdown():
            msg = MotorStatus()
            pub.publish(msg)
            rospy.sleep(1.0)
            
        rospy.loginfo("Stopping fake scitos_node")
    except rospy.ROSInterruptException:
        pass



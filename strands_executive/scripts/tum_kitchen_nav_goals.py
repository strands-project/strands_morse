#! /usr/bin/env python
import roslib; roslib.load_manifest('strands_executive')
import rospy

# Brings in the SimpleActionClient
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import *

import random

def simple_nav(x=0.0, y=0.0, z=0.0, qx=0.0, qy=0.0, qz=0.0, qw=1.0,
               frame_id="/map"):
    """ Simple navitgation function. Takes a goal in form of x/y/z coordinates,
    an orientation as quaternion (qx,qy,qz,qw), and a frame_id. The frame_id is
    used to specify the coordinate frame, e.g.: /map for global coordinates,
    /base_link for local/robot coordinates
    """
    
    client = actionlib.SimpleActionClient('move_base',
                                          move_base_msgs.msg.MoveBaseAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = move_base_msgs.msg.MoveBaseGoal()
    
    goal.target_pose.header.frame_id = frame_id
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw
    
    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    client.get_result()

    # Returns the result of executing the action
    return client

def perceive():
    rospy.loginfo("PERCEIVE")
    rospy.sleep(1)
    pass


if __name__ == '__main__':
    try:
        rospy.init_node('simple_nav')

        place = random.randint(1,4)
        
        if (place == 1):
            rospy.loginfo("Goal: behind counter")
            ac = simple_nav(x=0.0, y=-3.0, z=0.0, qx=0.0, qy=0.0, qz=0.0, qw=1.0,frame_id="/map")
        elif (place == 2):
            rospy.loginfo("Goal: in front of counter")
            ac = simple_nav(x=3.0, y=-3.0, z=0.0, qx=0.0, qy=0.0, qz=1.0, qw=0.0,frame_id="/map")
        elif (place == 3):
            rospy.loginfo("Goal: workplace one")
            ac = simple_nav(x=0.0, y=3.0, z=0.0, qx=0.0, qy=0.0, qz=0.9, qw=0.4,frame_id="/map")       
        else: #(place==4)
            rospy.loginfo("Goal: workplace two")
            ac = simple_nav(x=3.0, y=3.0, z=0.0, qx=0.0, qy=0.0, qz=0.7, qw=0.7,frame_id="/map")

        
        if (ac.get_state() == actionlib_msgs.msg.GoalStatus.SUCCEEDED):
            rospy.loginfo("Succeeded!")
            perceive()
            rospy.loginfo("Goal: go home")
            ac2 = simple_nav(x=0.0, y=0.0, z=0.0, qx=0.0, qy=0.0, qz=0.0, qw=1.0, frame_id="/map")
            if (ac2.get_state() == actionlib_msgs.msg.GoalStatus.SUCCEEDED):
                rospy.loginfo("Succeeded! At home!")
        
    except rospy.ROSInterruptException:
        rospy.logerror("program interrupted before completion")

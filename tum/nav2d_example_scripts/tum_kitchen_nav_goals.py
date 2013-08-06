#! /usr/bin/env python
import roslib; roslib.load_manifest('strands_morse')
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
    """Add Semantic camera here!"""
    rospy.loginfo("PERCEIVE")
    rospy.sleep(1)
    pass


def places():
    return {
        'counter_behind'   : {'x':0.0, 'y':-3.0, 'z':0.0, 'qx':0.0, 'qy':0.0, 'qz':0.0, 'qw':1.0},
        'counter_in_front' : {'x':3.0, 'y':-3.0, 'z':0.0, 'qx':0.0, 'qy':0.0, 'qz':1.0, 'qw':0.0},
        'workplace_one'    : {'x':0.0, 'y':3.0,  'z':0.0, 'qx':0.0, 'qy':0.0, 'qz':0.9, 'qw':0.4},
        'workplace_two   ' : {'x':3.0, 'y':3.0,  'z':0.0, 'qx':0.0, 'qy':0.0, 'qz':0.7, 'qw':0.7},
        }

def pose_at(place):
    return places().get(place, {'x':0.0, 'y':0.0, 'z':0.0, 'qx':0.0, 'qy':0.0, 'qz':0.0, 'qw':1.0}) # default pose

if __name__ == '__main__':
    try:
        rospy.init_node('simple_nav')

        plan_length = random.randint(1,len(places()))

        plan = random.sample(places().keys(), plan_length)

        rospy.loginfo("Plan: %s", plan)
        
        for place in plan:
            rospy.loginfo("Current goal: %s", place)
            pose = pose_at(place)
            ac = simple_nav(pose['x'], pose['y'], pose['z'],
                            pose['qx'], pose['qy'], pose['qz'], pose['qw'],
                            frame_id="/map")
            if (ac.get_state() == actionlib_msgs.msg.GoalStatus.SUCCEEDED):
                rospy.loginfo("Reached goal")
                perceive()

        rospy.loginfo("Accomplished plan. Go home...")
        
        pose = pose_at('default place')
        ac = simple_nav(pose['x'], pose['y'], pose['z'],
                        pose['qx'], pose['qy'], pose['qz'], pose['qw'],
                        frame_id="/map")
        if (ac.get_state() == actionlib_msgs.msg.GoalStatus.SUCCEEDED):
            rospy.loginfo("At home. Done!")
                
    except rospy.ROSInterruptException:
        rospy.logerror("program interrupted before completion")

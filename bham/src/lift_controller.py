#! /usr/bin/env python3.3
"""
An over simplified lift controller.

Controlls the lift in morse using a socket connection, and subscribes to:

/lift_sim/[command|call]floor : std_messages/Bool

where floor is [B|G|1|2].

The topics correspond to a user pressing the "call" buton on the outside of the lift on floor, or the "command" button on the inside of the lift to got to "floor". The lift travels in the order requested, and waits 8 seconds before closing the door.

"""

import sys
import rospy
from std_msgs.msg import Bool
import pymorse
import imp

rospy.init_node('lift_controller')
doors=['B','G','1','2']

lift_commands=[0]

def on_floor_call_command(data, args):
    (type,floor)=args
    """ On the press of the call or inside command button for lift..."""
    rospy.loginfo("[Lift Controller] Lift %s: To floor %s"%(type, doors[floor]))
    
    if floor in lift_commands:
        return
    lift_commands.append(floor)

    
for t in ["call","command"]:
    for i in range(0,4):
        rospy.Subscriber("/lift_sim/%s%s"%(t,doors[i]), Bool, on_floor_call_command, callback_args=(t,i))

morse = None

while not rospy.is_shutdown():
    rospy.loginfo("[Lift Controller] Waiting for Morse...")
    if pymorse.Morse._asyncore_thread is not None:
        # This is a strange hack that is required because of some bug in pymorse.
        # The async thread created by pymorse needs to be forced to recreate
        # when we start a new connection.
        rospy.loginfo("[Lift Controller] Crikey")
        pymorse.Morse._asyncore_thread.join()
        pymorse.Morse._asyncore_thread = None
    try:
        with pymorse.Morse() as morse:

            rospy.loginfo ("[Lift Controller] Ready.")

            while not rospy.is_shutdown():
                if len(lift_commands)>1:
                    rospy.loginfo("[Lift Controller] Closing door %s"%doors[lift_commands[0]])
                    morse.rpc('lift.door%s'%doors[lift_commands[0]],'change_door_state',0)
                    lift_commands=lift_commands[1:]
                    rospy.loginfo("[Lift Controller] Moving to floor %s"%doors[lift_commands[0]])
                    morse.rpc('lift.platform','move_to_floor',lift_commands[0]-1)
                    rospy.loginfo("[Lift Controller] Opening door %s"%doors[lift_commands[0]])
                    morse.rpc('lift.door%s'%doors[lift_commands[0]],'change_door_state',1)
                    rospy.sleep(8)
    except Exception as e:
        rospy.loginfo("[Lift Controller] " + str(e) + " : will retry.")
        rospy.sleep(0.5)
    



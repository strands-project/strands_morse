#! /usr/bin/env python3
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

from pymorse import Morse
rospy.init_node('lift_controller')
doors=['B','G','1','2']

lift_commands=[0]

def on_floor_call_command(data, args):
    (type,floor)=args
    """ On the press of the call or inside command button for lift..."""
    rospy.loginfo("Lift %s: To floor %s"%(type, doors[floor]))
    
    if floor in lift_commands:
        return
    lift_commands.append(floor)

    
for t in ["call","command"]:
    for i in range(0,4):
        rospy.Subscriber("/lift_sim/%s%s"%(t,doors[i]), Bool, on_floor_call_command, callback_args=(t,i))

morse = None
while morse is None:
    try:
        morse = Morse()
    except ConnectionError as e:# ConnectionError as e:
        rospy.loginfo("Waiting for Morse...")
        print("[!!!!!] ",e,"Waiting for Morse...")
        rospy.sleep(3)
    
while not rospy.is_shutdown():
    if len(lift_commands)>1:
        rospy.loginfo("Closing door %s"%doors[lift_commands[0]])
        morse.rpc('lift.door%s'%doors[lift_commands[0]],'change_door_state',0)
        lift_commands=lift_commands[1:]
        rospy.loginfo("Moving to floor %s"%doors[lift_commands[0]])
        morse.rpc('lift.platform','move_to_floor',lift_commands[0]-1)
        rospy.loginfo("Opening door %s"%doors[lift_commands[0]])
        morse.rpc('lift.door%s'%doors[lift_commands[0]],'change_door_state',1)
        rospy.sleep(8)


morse.close()

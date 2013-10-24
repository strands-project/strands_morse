#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
import random

#robot = Ranger()
robot = Scitosa5()

# tum_kitchen
robot.translate(x=2.5, y=3.2, z=0.0)

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=1.0)


cup1 = PassiveObject('props/kitchen_objects','Cup_Blue')
cup1.properties(Object = True, Type = 'Cup')
cup1.translate(x=3.3,
               y=0.8,
               z=0.95)

# cup on workplace one
# cup2 = PassiveObject('props/kitchen_objects','Cup_Gray')
# cup2.properties(Object = True, Type = 'Cup')
# cup2.translate(x=2.0,
#                y=8.0,
#                z=0.8)

# cup on workplace two 
# cup3 = PassiveObject('props/kitchen_objects','Cup_Ocher')
# cup3.properties(Object = True, Type = 'Cup')
# cup3.translate(x=5.0,
#                y=8.0,
#                z=0.8)

# Set the environment
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])

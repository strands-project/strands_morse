#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
from strands_sim.builder.robots import HumanStrands

#robot = Ranger()
robot = Scitosa5()

# tum_kitchen
robot.translate(x=0, y=-2, z=0.0)

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=1.0)

human=HumanStrands()
human.use_world_camera()
human.translate(x=0, y=-1, z=0.1)

pose = Pose()
human.append(pose)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/StudyRestaurant.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([0, 10, 6])
env.aim_camera([1.0470, 0, 3.1])

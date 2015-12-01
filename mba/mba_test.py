#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5(with_cameras=Scitosa5.WITHOUT_CAMERAS)

robot.translate(x=0.1, y=0.1, z=0.1)
rpose = Pose()
robot.append(rpose)
rpose.add_stream('ros', method="morse.middleware.ros.pose.TFPublisher", frame_id='/world', child_frame_id="/robot")

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=0.0)

for i in range(10):
    exec("""
chair%i = (PassiveObject(os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/Chair.blend')))
chair%i.properties(Object = True)
chair%i.translate(x=10, y=10, z=0.0)
chair%i.rotate(x= 0.0, y=0.0, z=1.57)
""" % (i,i,i,i))

for i in range(10):
    exec("""
officechair%i = (PassiveObject(os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/OfficeChair.blend')))
officechair%i.properties(Object = True)
officechair%i.translate(x=30, y=10, z=0.0)
officechair%i.rotate(x= 0.0, y=0.0, z=1.57)
""" % (i,i,i,i))

for i in range(10):
    exec("""
wheelchair%i = (PassiveObject(os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/WheelChair.blend')))
wheelchair%i.properties(Object = True)
wheelchair%i.translate(x=20, y=10, z=0.0)
wheelchair%i.rotate(x=0.0, y=0.0, z=1.57)
""" % (i,i,i,i))

for i in range(10):
    exec("""
statichuman%i = (PassiveObject(os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/WomanStanding.blend')))
statichuman%i.properties(Object = True)
statichuman%i.translate(x=40, y=10, z=0.0)
statichuman%i.rotate(x=0.0, y=0.0, z=1.57)
""" % (i,i,i,i))

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/move_base_arena.blend')
env = Environment(model_file,fastmode=True)
env.set_camera_location([0.0,-2.5,15.0])
env.set_camera_rotation([0.16742943514, 0.0,0.0])
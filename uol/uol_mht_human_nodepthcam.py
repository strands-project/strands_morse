#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5
from strands_sim.builder.robots import HumanStrands

#robot = Ranger()
robot = Scitosa5(with_cameras=Scitosa5.WITHOUT_DEPTHCAMS)
semanticcamera = SemanticCamera()
robot.append(semanticcamera)
semanticcamera.translate(0.00, 0.02, 1.5)
semanticcamera.rotate(0.0, 0.0, 0.0)
semanticcamera.properties(relative=True, cam_width=640, cam_height=480, cam_far=20, cam_near= 0.1, cam_focal=25)
semanticcamera.add_interface('ros', topic= "/humancam", frame_id= "/head_xtion_rgb_optical_frame")

# tum_kitchen
robot.translate(x=2.5, y=3.2, z=0.1)
rpose = Pose()
robot.append(rpose)
rpose.add_stream('ros', method="morse.middleware.ros.pose.TFPublisher", frame_id='/world', child_frame_id="/robot")

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=1.0)

human=Human()
human.use_world_camera()
human.translate(x=4.5, y=3.2, z=0.1)
human.properties(Object = True)

pose = Pose()
human.append(pose)

pose.add_stream('ros', method="morse.middleware.ros.pose.TFPublisher", frame_id='/world', child_frame_id="/human")
pose.add_stream('ros', frame_id='/world')


# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/MHTThirdFloor.blend')
env = Environment(model_file,fastmode=False)
env.aim_camera([1.0470, 0, 0.7854])

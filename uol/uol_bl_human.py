#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5(with_cameras=Scitosa5.WITH_OPENNI)
semanticcamera = SemanticCamera()
robot.append(semanticcamera)
semanticcamera.translate(0.00, 0.02, 1.5)
semanticcamera.rotate(0.0, 0.0, 0.0)
semanticcamera.properties(relative=True, cam_width=640, cam_height=480, cam_far=20, cam_near= 0.1, cam_focal=25)
semanticcamera.add_interface('ros', topic= "/humancam", frame_id= "/head_xtion_rgb_optical_frame")

# tum_kitchen
robot.translate(x=-11, y=-2.5, z=0.1)
#robot.translate(x=1, y=7.62, z=0.0)
robot.rotate(0,0,3.141592)
rpose = Pose()
robot.append(rpose)
rpose.add_stream('ros', method="morse.middleware.ros.pose.TFPublisher", frame_id='/world', child_frame_id="/robot")

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=0.01)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(-11.15,-2.5,0.285)
docking_station.rotate(0,0,3.141592)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(-11.25,-2.5,1.75)
docking_station_label.rotate(1.57,0,1.57)

human=Human()
human.use_world_camera()
human.translate(x=-7, y=-2.5, z=0.1)
human.properties(Object = True)

pose = Pose()
human.append(pose)
motion = MotionVW()
human.append(motion)
motion.properties(ControlType = 'Velocity')
motion.add_stream('ros')

pose.add_stream('ros', method="morse.middleware.ros.pose.TFPublisher", frame_id='/world', child_frame_id="/human")
pose.add_stream('ros', frame_id='/world')

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/BL.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([-2.0, 0.0, 6.0])
env.aim_camera([1.0470, 0, 1.7854])

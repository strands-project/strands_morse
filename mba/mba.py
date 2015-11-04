#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5()

#robot.translate(x=0.1, y=0.1, z=0.1)
robot.translate(x=-1.5, y=2.6, z=0.1)
robot.rotate(0,0,1.57)
rpose = Pose()
robot.append(rpose)
rpose.add_stream('ros', method="morse.middleware.ros.pose.TFPublisher", frame_id='/world', child_frame_id="/robot")



# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=0.0)

#docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
#docking_station.properties(Object = True)
#docking_station.properties(ChargingZone = True)
#docking_station.translate(1,7.85,0.235)
#docking_station.rotate(0,0,1.57)

#docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
#docking_station_label.properties(Object = True)
#docking_station_label.translate(1,7.95,1.75)
#docking_station_label.rotate(1.57,0,0)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/move_base_arena.blend')
env = Environment(model_file,fastmode=False)
env.set_camera_location([0.0,-2.5,15.0])
env.set_camera_rotation([0.16742943514, 0.0,0.0])
#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""
import math
from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5(with_cameras=Scitosa5.WITH_OPENNI)

robot.translate(x=8.6, y=4, z=1)
#robot.translate(x=1, y=7.62, z=0.0)
robot.rotate(0, 0, 3.141592)

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=0.015)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(8.4, 4, 0.385)
docking_station.rotate(0, 0, math.pi + 0.2)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(8.3, 4, 1.75)
docking_station_label.rotate(math.pi/2, 0, math.pi/2 + 0.17)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/thecollectionscaled.blend')
env = Environment(model_file,fastmode=False)
env.set_camera_location([7.0, 15.0, 15.0])
env.set_camera_rotation([math.pi/6, 0, math.pi])

#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5(with_cameras = Scitosa5.WITH_OPENNI)

# tum_kitchen
robot.translate(x=0.5, y=23.2, z=0.1)

#robot.translate(x=1, y=7.62, z=0.0)
#robot.rotate(0,0,1.57)

# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=0.01)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(2.479,28.4,0.245)
docking_station.rotate(0,0,1.229)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(2.49,28.4755,1.75)
docking_station_label.rotate(1.57,0,5.9422)

docking_station2 = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station2.properties(Object = True)
docking_station2.properties(ChargingZone = True)
docking_station2.translate(-7.4979,-15.014,0.245)
docking_station2.rotate(0,0,2.8315)

docking_station_label2 = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label2.properties(Object = True),
docking_station_label2.translate(-7.57,-15.002,1.75)
docking_station_label2.rotate(1.57,0,1.2617)


# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/tsc.blend')
env = Environment(model_file,fastmode=False)
env.place_camera([-2.0, 0.0, 6.0])
env.aim_camera([1.0470, 0, 0.0])

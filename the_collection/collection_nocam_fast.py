#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5


for r in range(0,4):
    robot = Scitosa5(with_cameras=Scitosa5.WITHOUT_CAMERAS,
                     prefix="/robot_%02d" % r)
    robot.translate(x=2.5, y=3 + r, z=0.1)
    robot.battery.properties(DischargingRate=0.01)



#create_robot(x=2.5, y=3.2, z=0.1, prefix="")
#create_robot(x=2.5, y=4.2, z=0.1, prefix="scitos_2")

# docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
# docking_station.properties(Object = True)
# docking_station.properties(ChargingZone = True)
# docking_station.translate(1,7.85,0.235)
# docking_station.rotate(0,0,1.57)

# docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
# docking_station_label.properties(Object = True)
# docking_station_label.translate(1,7.95,1.75)
# docking_station_label.rotate(1.57,0,0)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/MHTThirdFloor.blend')
env = Environment(model_file,fastmode=True)
env.aim_camera([1.0470, 0, 0.7854])

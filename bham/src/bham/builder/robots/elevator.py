from morse.builder import *
from bham.builder.actuators import Platform,SlidingDoor

class Elevator(Robot):
    """
    """
    def __init__(self, debug = True):
        Robot.__init__(self, 'bham/robots/elevator.blend')
        self.properties(classpath = "bham.robots.elevator.Elevator")

        ###################################
        # Actuators
        ###################################
        self.platform  = Platform()
        self.append(self.platform)
        self.door2=SlidingDoor()
        self.door2.properties(left_panel="Ldoor2",right_panel="Rdoor2")
        self.append(self.door2)
        self.door1=SlidingDoor()
        self.door1.properties(left_panel="Ldoor1",right_panel="Rdoor1")
        self.append(self.door1)
        self.doorG=SlidingDoor()
        self.doorG.properties(left_panel="Ldoor0",right_panel="Rdoor0")
        self.append(self.doorG)
        self.doorB=SlidingDoor()
        self.doorB.properties(left_panel="Ldoor-1",right_panel="Rdoor-1")
        self.append(self.doorB)

        ###################################
        # Sensors
        ###################################
	# TODO: add button sensors and door-blocked sensor

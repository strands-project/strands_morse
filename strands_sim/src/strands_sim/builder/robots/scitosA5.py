from morse.builder import *

class Scitosa5(Robot):
    """
    A template robot model for scitosA5, with a motion controller and a pose sensor.
    """
    def __init__(self, debug = True):

        # scitosA5.blend is located in the data/robots directory
        Robot.__init__(self, 'strands_sim/robots/scitosA5.blend')
        #Robot.__init__(self, '/home/lars/work/strands/ranger_sim/data/ranger_sim/robots/ranger.blend')
        self.properties(classpath = "strands_sim.robots.scitosA5.Scitosa5")

        ###################################
        # Actuators
        ###################################

        # Check here the other available actuators:
        # http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
        #self.motion = MotionXYW()
        #self.append(self.motion)

        # Optionally allow to move the robot with the keyboard
        #if debug:
        #    keyboard = Keyboard()
        #    self.append(keyboard)

        ###################################
        # Sensors
        ###################################

        #self.pose = Pose()
        #self.append(self.pose)


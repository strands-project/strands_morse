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

        # The list of the main methods to manipulate your components
        # is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
        self.add_interface('ros')

        ###################################
        # Actuators
        ###################################

        # Motion control
        self.motion = MotionXYW()
        self.append(self.motion)
        self.motion.add_interface('ros', topic='/cmd_vel')

        # Keyboard control
        self.keyboard = Keyboard()
        self.append(self.keyboard)

        ###################################
        # Sensors
        ###################################

        # Odometry
        self.odometry = Odometry()
        self.append(self.odometry)
        self.odometry.add_interface('ros', topic="/odom")

        # Laserscanner
        self.scan = Hokuyo()
        #scan.translate(x=0.275, z=0.252)
        #scan.translate(x=0.65, z=-0.60)
        self.scan.translate(x=0.30, z=0.386)
        self.append(self.scan)
        self.scan.properties(Visible_arc = False)
        self.scan.properties(laser_range = 30.0)
        self.scan.properties(resolution = 1.0)
        self.scan.properties(scan_window = 180.0)
        self.scan.create_laser_arc()
        self.scan.add_interface('ros', topic='/scan')

        #self.pose = Pose()
        #self.append(self.pose)


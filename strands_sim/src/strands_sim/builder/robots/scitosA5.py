from morse.builder import *
from morse.builder.bpymorse import *

class Scitosa5(Robot):
    # camera configuration
    WITH_OPENNI = 0
    WITH_CAMERAS = 1
    WITHOUT_DEPTHCAMS = 2
    WITHOUT_CAMERAS = 3

    # topic names
    MOTION_TOPIC          = '/cmd_vel'
    ODOMETRY_TOPIC        = '/odom'
    PTU_TOPIC             = '/ptu'
    PTU_POSE_TOPIC        = '/ptu/state'
    BATTERY_TOPIC         = '/battery_state'
    SCAN_TOPIC            = '/scan'
    VIDEOCAM_TOPIC        = '/head_xtion/rgb'
    VIDEOCAM_TOPIC_SUFFIX = '/image_mono'
    SEMANTICCAM_TOPIC     = '/semcam'
    DEPTHCAM_TOPIC        = '/head_xtion/depth/points'

    # frame id's
    DEPTHCAM_FRAME_ID = '/head_xtion_depth_optical_frame'
    VIDEOCAM_FRAME_ID = '/head_xtion_rgb_optical_frame'
    SEMANTICCAM_FRAME_ID = '/head_xtion_rgb_optical_frame'
        
    """
    A template robot model for scitosA5
    """
    def __init__(self, with_cameras = 1):
        if with_cameras == Scitosa5.WITH_OPENNI:
            Scitosa5.VIDEOCAM_TOPIC        = '/head_xtion/rgb8'
            Scitosa5.DEPTHCAM_TOPIC        = '/head_xtion/depth/points_raw'

        # scitosA5.blend is located in the data/robots directory
        Robot.__init__(self, 'strands_sim/robots/scitos.blend')

        self.properties(classpath = "strands_sim.robots.scitosA5.Scitosa5")

        # The list of the main methods to manipulate your components
        # is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
        self.add_interface('ros')

        ###################################
        # Actuators
        ###################################

        # Motion control
        self.motion = MotionVW()
        self.append(self.motion)
        self.motion.properties(ControlType = 'Position') # default 'Velocity' causes motion problems
        self.motion.add_interface('ros', topic= Scitosa5.MOTION_TOPIC)

        # Keyboard control
        self.keyboard = Keyboard()
        self.append(self.keyboard)

        self.ptu = PTU() # creates a new instance of the actuator
        self.append(self.ptu)
        self.ptu.translate(-0.075, 0, 1.585)
        self.ptu.rotate(0, 0, 0)
        self.ptu.add_interface('ros', topic= Scitosa5.PTU_TOPIC)
        self.ptu.properties(Tolerance= 0.00089759763795882463)

        ###################################
        # Sensors
        ###################################

        # PTU pose
        self.ptu_pose = PTUPosture('ptu_pose')
        self.ptu.append(self.ptu_pose)
        self.ptu_pose.add_interface('ros', topic= Scitosa5.PTU_POSE_TOPIC)
        
        # Battery
        self.battery = BatteryStateSensor()
        self.battery.translate(x=0.00,y=0.0,z=0.0)
        self.battery.properties(Range = 0.45)
        self.append(self.battery)
        self.battery.add_interface('ros', topic= Scitosa5.BATTERY_TOPIC)
        self.battery.properties(DischargingRate=0.01)

        # Odometry
        self.odometry = Odometry()
        self.append(self.odometry)
        self.odometry.add_interface('ros', topic= Scitosa5.ODOMETRY_TOPIC)
        #self.odometry.frequency(9.9)
        
        # Laserscanner
        self.scan = Hokuyo()
        self.scan.translate(x=0.07, z=0.365)
        self.append(self.scan)
        self.scan.properties(Visible_arc = False)
        self.scan.properties(laser_range = 30.0)
        self.scan.properties(resolution = 1.0)
        self.scan.properties(scan_window = 180.0)
        self.scan.create_laser_arc()
        self.scan.add_interface('ros', topic= Scitosa5.SCAN_TOPIC)

        if with_cameras < Scitosa5.WITHOUT_CAMERAS:
            self.videocam = VideoCamera()
            self.ptu.append(self.videocam)
            self.videocam.translate(0.00, -0.045, 0.0945)
            self.videocam.rotate(0, 0, 0)
            if with_cameras == Scitosa5.WITH_OPENNI:
                self.videocam.properties(cam_width=640, cam_height=480, cam_focal=26.25)
                self.videocam.frequency(20)
            else:
                self.videocam.properties(cam_width=640, cam_height=480)
                self.videocam.frequency(30)
            self.videocam.add_interface('ros',
                                        topic= Scitosa5.VIDEOCAM_TOPIC,
                                        topic_suffix= Scitosa5.VIDEOCAM_TOPIC_SUFFIX,
                                        frame_id= Scitosa5.VIDEOCAM_FRAME_ID)
            
            # Semantic Camera
            self.semanticcamera = SemanticCamera()
            self.ptu.append(self.semanticcamera)
            self.semanticcamera.translate(0.00, 0.02, 0.0945)
            self.semanticcamera.rotate(0.0, 0.0, 0.0)
            self.semanticcamera.properties(cam_width=640, cam_height=480, cam_far=2.5, cam_near= 0.8, cam_focal=69.5)
            self.semanticcamera.add_interface('ros', topic= Scitosa5.SEMANTICCAM_TOPIC, frame_id= Scitosa5.SEMANTICCAM_FRAME_ID)
            
            if with_cameras < Scitosa5.WITHOUT_DEPTHCAMS:
                # Depth camera
                self.depthcam = DepthCamera() # Kinect() RVIZ crashes when depthcam data is visualized!?
                self.ptu.append(self.depthcam)
                self.depthcam.translate(0.00, 0.02, 0.0945)
                #self.append(self.depthcam)
                #self.depthcam.translate(0.09, 0.02, 1.6795)

                # set the near clip very low,
                # otherwise the depthcam scans through objects within the clipping area!
                self.depthcam.properties(cam_near = 0.1)

                # workaround for point cloud with offset
                if with_cameras == Scitosa5.WITH_OPENNI:
                    self.depthcam.properties(cam_width = 640, cam_height = 480, cam_focal = 28.5)
                    bpy.context.scene.render.resolution_x = 640
                    bpy.context.scene.render.resolution_y = 480
                else:
                    self.depthcam.properties(cam_width = 128, cam_height = 128)
                    bpy.context.scene.render.resolution_x = 128
                    bpy.context.scene.render.resolution_y = 128

                self.depthcam.rotate(0, 0, 0)
                self.depthcam.add_interface('ros', topic= Scitosa5.DEPTHCAM_TOPIC, frame_id= Scitosa5.DEPTHCAM_FRAME_ID, tf='False')





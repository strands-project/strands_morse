#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from tf import TransformListener
import json

class PoseTransformer:

    def set_visible(self,data):
        d=json.loads(data.data)
        if len(d)>0:
            self.visible=True
        else:
            self.visible=False


    def callback(self,data):
        rospy.logdebug(rospy.get_caller_id()+"I heard something from frame %s",data.header.frame_id)
        if self.visible:
            t = self.tf.getLatestCommonTime(self.target_tf, data.header.frame_id)
            data.header.stamp=t
            new_pose=self.tf.transformPose(self.target_tf,data)
            self.pub.publish(new_pose)
        else:
            rospy.logdebug("human not visible at the moment")


    def __init__(self):
        rospy.init_node('posetransformer_node', anonymous=True)
        self.in_topic = rospy.get_param('~in', '/human/pose')
        self.out_topic = rospy.get_param('~out', '/human/transformed')
        self.target_tf = rospy.get_param('~target', '/robot')
        self.sem_cam = rospy.get_param('~sem_cam', '/humancam')
        self.sub = rospy.Subscriber(self.in_topic, PoseStamped, self.callback)
        self.sub = rospy.Subscriber(self.sem_cam, String, self.set_visible)
        self.pub = rospy.Publisher(self.out_topic, PoseStamped)
        self.tf = TransformListener()
        self.visible = True

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    PoseTransformer()

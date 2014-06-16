#include <ros/ros.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <sensor_msgs/CameraInfo.h>

ros::Publisher image_pub;
ros::Publisher camera_info_pub;

void img_callback(const sensor_msgs::Image::ConstPtr& image_msg)
{
    size_t width = 640;
	size_t height = 480;
    image_pub.publish(image_msg);
    
    // ros camera parameters
    sensor_msgs::CameraInfo info;
    info.width = width;
    info.height = height;
    info.distortion_model = "plumb_bob";
    info.K = {{525.0, 0.0, 319.5, 0.0, 525.0, 239.5, 0.0, 0.0, 1.0}};
    info.R = {{1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0}};
    info.P = {{525.0, 0.0, 319.5, 0.0, 0.0, 525.0, 239.5, 0.0, 0.0, 0.0, 1.0, 0.0}};
    double D[5] = {0.0,0.0,0.0,0.0,0.0};
    info.D.assign(&D[0], &D[0]+5);
    info.header.frame_id = image_msg->header.frame_id;
    info.header.stamp = image_msg->header.stamp;
    
    camera_info_pub.publish(info);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "generate_rgb");
	ros::NodeHandle n;
	
	ros::NodeHandle pn("~");
    std::string image_input;
    std::string camera;
    pn.param<std::string>("camera", camera, std::string("head_xtion"));
    std::string input = std::string("/") + camera + std::string("/rgb8/image_mono");
    std::string output = std::string("/") + camera + std::string("/rgb/image_raw");
    
    ros::Subscriber sub = n.subscribe(input, 1, img_callback);
    image_pub = n.advertise<sensor_msgs::Image>(output, 1);
    camera_info_pub = n.advertise<sensor_msgs::CameraInfo>(std::string("/") + camera + std::string("/rgb/camera_info"), 1000);
    
    ros::spin();
	
	return 0;
}

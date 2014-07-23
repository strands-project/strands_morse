#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <sensor_msgs/CameraInfo.h>

ros::Publisher image_pub;
ros::Publisher cloud_pub;
ros::Publisher camera_info_pub;

ros::Time last_stamp;
sensor_msgs::CameraInfo cam_info;
sensor_msgs::ImagePtr image;
bool initialized;

void pcd_callback(const sensor_msgs::PointCloud2::ConstPtr& cloud_msg)
{
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>());
    pcl::fromROSMsg(*cloud_msg, *cloud);
    
	size_t width = 640;
	size_t height = 480;
	cv::Mat temp_depth = cv::Mat::zeros(height, width, CV_16UC1);
    
    size_t n = cloud->points.size();
    Eigen::Vector3f p;
    int x, y;
    uint16_t z, curr_z;
    float f = 570; // focal length of /head_xtion/rgb/image_mono
    for (size_t i = 0; i < n; ++i) {
        p = cloud->points[i].getVector3fMap();
        x = int(f*p(0)/p(2) + 0.5) + width/2;
        y = int(f*p(1)/p(2) + 0.5) + height/2;
        if (x >= 0 && x < width && y >= 0 && y < height) {
            z = uint16_t(1000.0*p(2));
            curr_z = temp_depth.at<uint16_t>(y, x);
            if (curr_z == 0 || curr_z > z) {
                temp_depth.at<uint16_t>(y, x) = z;
            }
        }
    }
    cv_bridge::CvImage image_depth = cv_bridge::CvImage(cloud_msg->header, "16UC1", temp_depth);
    image = image_depth.toImageMsg();
    
    cam_info.width = width;
    cam_info.height = height;
    cam_info.distortion_model = "plumb_bob";
    cam_info.K = {{f, 0.0, 320.5, 0.0, f, 240.5, 0.0, 0.0, 1.0}};
    cam_info.R = {{1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0}};
    cam_info.P = {{f, 0.0, 320.5, 0.0, 0.0, f, 240.5, 0.0, 0.0, 0.0, 1.0, 0.0}};
    double D[5] = {0.0,0.0,0.0,0.0,0.0};
    cam_info.D.assign(&D[0], &D[0]+5);
    cam_info.header.frame_id = cloud_msg->header.frame_id;
    cam_info.header.stamp = cloud_msg->header.stamp;
    initialized = true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "generate_disparity");
	ros::NodeHandle n;
	
	ros::NodeHandle pn("~");
	std::string camera;
    pn.param<std::string>("camera", camera, std::string("head_xtion"));
    std::string input = std::string("/") + camera + std::string("/depth/points_raw");
    std::string output = std::string("/") + camera + std::string("/depth/image_raw");
    
	ros::Subscriber sub = n.subscribe(input, 1, pcd_callback);
    image_pub = n.advertise<sensor_msgs::Image>(output, 1);
    camera_info_pub = n.advertise<sensor_msgs::CameraInfo>(std::string("/") + camera + std::string("/depth/camera_info"), 1000);
    
    initialized = false;
    ros::Rate rate(20);
    while (n.ok()) {
        ros::spinOnce();
        if (initialized) {
            ros::Time now = ros::Time::now();
            ros::Duration duration = now - last_stamp;
            ros::Time stamp = last_stamp + duration;
            cam_info.header.stamp = stamp;
            camera_info_pub.publish(cam_info);
            image->header.stamp = stamp;
            image_pub.publish(image);
        }
        rate.sleep();
    }
	
	return 0;
}

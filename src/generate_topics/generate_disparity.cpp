#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <boost/thread/thread.hpp>
#include <tf/transform_listener.h>
#include <message_filters/subscriber.h>
#include <message_filters/time_synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>

ros::Publisher image_pub;
ros::Publisher cloud_pub;

tf::TransformListener* listener;

void callback(const sensor_msgs::Image::ConstPtr& image_msg, const sensor_msgs::PointCloud2::ConstPtr& cloud_msg)
{
    std::string dest_frame("/head_xtion_rgb_optical_frame");
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>());
    pcl::fromROSMsg(*cloud_msg, *cloud);
    
    tf::StampedTransform transform;
    try {
        //listener->transformPointCloud("/head_xtion_rgb_optical_frame", msg->header.stamp, *msg, msg->header.frame_id, cout);
        listener->lookupTransform (dest_frame, cloud_msg->header.frame_id, cloud_msg->header.stamp, transform);
    }
    catch (tf::TransformException ex) {
        ROS_INFO("%s",ex.what());
        return;
    }
    
    tf::Matrix3x3 basis = transform.getBasis();
    tf::Vector3 origin = transform.getOrigin();
    
    Eigen::Matrix3f ebasis;
    Eigen::Vector3f eorigin;
    for (size_t i = 0; i < 3; ++i) {
        eorigin(i) = origin.m_floats[i];
        for (size_t j = 0; j < 3; ++j) {
            ebasis(i, j) = basis.getRow(i).m_floats[j];
        }
    }
    
    // K matrix for /head_xtion/rgb/image_mono
    //Eigen::Matrix3f K;
    //K.setZero();
    //K(0, 0) = 700.0; K(0, 2) = 0.0;
    //K(1, 1) = 700.0; K(0, 2) = 0.0;
    //K(2, 2) = 1.0;
    
    boost::shared_ptr<sensor_msgs::Image> rgb_tracked_object;
	cv_bridge::CvImageConstPtr rgb_cv_img_boost_ptr;
	try {
		rgb_cv_img_boost_ptr = cv_bridge::toCvShare(*image_msg, rgb_tracked_object);
	}
	catch (cv_bridge::Exception& e) {
		ROS_ERROR("cv_bridge exception: %s", e.what());
		return;
	}
	size_t width = rgb_cv_img_boost_ptr->image.size().width;
	size_t height = rgb_cv_img_boost_ptr->image.size().height;
	cv::Mat temp_depth = cv::Mat::zeros(height, width, CV_16UC1);
    
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr ccloud(new pcl::PointCloud<pcl::PointXYZRGB>());
    size_t n = cloud->points.size();
    ccloud->points.resize(n);
    Eigen::Vector3f p;
    int x, y;
    float f = 700.0; // focal length of /head_xtion/rgb/image_mono
    for (size_t i = 0; i < n; ++i) {
        pcl::PointXYZ& spoint = cloud->points[i];
        pcl::PointXYZRGB& dpoint = ccloud->points[i];
        p = eorigin + ebasis*spoint.getVector3fMap();
        dpoint.getVector3fMap() = p;
        //p = K*p;
        //p = 1.0/p(2)*p;
        x = int(f*p(0)/p(2)) + width/2;
        y = int(f*p(1)/p(2)) + height/2;
        
        if (x >= 0 && x < width && y >= 0 && y < height) {
            cv::Vec3b bgrPixel = rgb_cv_img_boost_ptr->image.at<cv::Vec3b>(y, x);
            dpoint.r = bgrPixel[0];
            dpoint.g = bgrPixel[1];
            dpoint.b = bgrPixel[2];
            temp_depth.at<uint16_t>(y, x) = uint16_t(1000.0*p(2));
        }
        else {
            dpoint.r = 255;
            dpoint.g = 0;
            dpoint.b = 0;
        }
    }
    
    sensor_msgs::PointCloud2 cout;
    pcl::toROSMsg(*ccloud, cout);
    cout.header = cloud_msg->header;
    cout.header.frame_id = dest_frame;
    cloud_pub.publish(cout);
    
    cv_bridge::CvImage image_depth = cv_bridge::CvImage(image_msg->header, "16UC1", temp_depth);
    image_pub.publish(image_depth.toImageMsg());
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "generate_disparity");
	ros::NodeHandle n;
	
	ros::NodeHandle pn("~");
	std::string cloud_input;
    pn.param<std::string>("input", cloud_input, std::string("/head_xtion/depth/points"));
    std::string image_input;
    pn.param<std::string>("input", image_input, std::string("/head_xtion/rgb/image_mono"));
    std::string output;
    pn.param<std::string>("output", output, std::string("/head_xtion/depth/image"));
    
    listener = new tf::TransformListener();
    
    typedef message_filters::sync_policies::ApproximateTime<sensor_msgs::Image, sensor_msgs::PointCloud2> MySyncPolicy;
    message_filters::Subscriber<sensor_msgs::Image> image_sub(n, image_input, 5);
    message_filters::Subscriber<sensor_msgs::PointCloud2> cloud_sub(n, cloud_input, 5);
    message_filters::Synchronizer<MySyncPolicy> sync(MySyncPolicy(1), image_sub, cloud_sub);
    sync.registerCallback(&callback);
    
	//ros::Subscriber sub = n.subscribe(input, 1, callback);
    image_pub = n.advertise<sensor_msgs::Image>(output, 1);
    cloud_pub = n.advertise<sensor_msgs::PointCloud2>("/rgb_cloud", 1);
    
    ros::spin();
	
	return 0;
}

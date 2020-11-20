#include "ros/ros.h"
#include "std_msgs/String.h"
#include "chat_my2/test.h"	//前面是包的名字，后面是.msg的名字，注意这里后缀要将.msg改为.h

void chatterCallback_1(const chat_my2::test::ConstPtr& msg)//注意此处要更改话题消息类型
{
	//打印收到的消息
	ROS_INFO("I heard:x=%f,y=%f,z=%s",msg->x,msg->y,msg->s);
}

int main(int argc,char **argv)
{
	ros::init(argc,argv,"listener");
	ros::NodeHandle n;
	
	ros::Subscriber sub=n.subscribe("chatter",1000,chatterCallback_1);	//创建一个Subscriber，订阅名为chatter，回调函数

	ros::spin();	//循环等待回调函数
	return 0;
}


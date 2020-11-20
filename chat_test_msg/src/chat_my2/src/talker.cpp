#include <sstream>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "chat_my2/test.h"	//前面是包的名字，后面是.msg的名字，注意这里后缀要将.msg改为.h

int main(int argc,char **argv)
{
	ros::init(argc,argv,"talker");	//节点初始化
	ros::NodeHandle n;	//创建节点句柄

	
	ros::Publisher chatter_pub=n.advertise<chat_my2::test>("chatter",1000);///创建publisher，发布名为chatter,类型为chat_my::test(这里是自己定义的话题消息，注意格式),队列大小为1000
	chat_my2::test num; //定义一个话题消息变量
	
	ros::Rate lopp_rate(10);	//设置循环的频率10hz，调用Rate::sleep()时，会休眠一定时间保证频率

	int count=0.0;
	while(ros::ok)	//节点有异常时，ros::ok 返回false
	{
		//初始化要发布的消息
		num.x=10.1;
		num.y=count;
		num.s=''talker'';
		
		//发布消息
		chatter_pub.publish(num);
		ROS_INFO("I heard:x=%f,y=%f,z=[%s]",num.x,num.y,num.s);

		//循环等待回调函数
		ros::spinOnce();

		//按照循环频率延时
		lopp_rate.sleep();
		++count;

	}
	return 0;

}


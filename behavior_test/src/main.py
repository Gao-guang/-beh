#-*- coding: UTF-8 -*-
import rospy
import rospy
from core import DBlackboard, Role
from std_msgs.msg import String


if __name__ == '__main__':
    # initialize ROS node
    rospy.init_node('behavior_node', log_level=rospy.INFO)
    rate = rospy.Rate(30)

    # initialize behavior
    bb = DBlackboard()
    behavior = Role(bb)

    # run ros node
    while not rospy.is_shutdown():
        bb.reset()
        behavior.step()
        bb.publish()
        rate.sleep()
# -*- coding: utf-8 -*-
import rospy

from sensor_msgs.msg import Joy
from std_msgs.msg import String

from btree.core import Blackboard

from math import sqrt


class DBlackboard(Blackboard):
    """
    Special implementation of Blackboard class for humanoid project of ZJUDancer.
    """

    def __init__(self):
        super(DBlackboard, self).__init__()
        # determined actions
        self.action_cmd = "go"

        # rospy.Subscriber("/joy", Joy, self.update_joy)
        # self.action_cmd_publisher = rospy.Publisher(
        #     '/dbehavior_{}/ActionCommand'.format(self.id),
        #     ActionCommand,
        #     queue_size=1)

    def reset(self):
        """Reset action command for new step."""
        # self.action_cmd = ActionCommand()
        # self.action_cmd.bodyCmd = self.action_generator.crouch()
        # self.behavior_info = BehaviorInfo()
        # self.behavior_info.current_role = self.current_role
        # self.behavior_info.time_since_last_kick = self.timer_kick_success.elapsed(
        # )
        # if not self.lower_board_lost:
        #     self.set_state('playing')
        # else:
        #     self.set_state('inactive')

    def publish(self):
        rospy.loginfo("publish ing ")


    def update_joy(self, msg):
        """
        Callback function for receiving joy signal.
        :param msg: joy signal
        :type msg: Joy
        """
        # self.joy_info = msg
        # if self.joy_info.buttons[7]:  # 'start' button
        #     # print('start')
        #     self.timer_joystick_started.restart()
        #     self.joystick_started = True
        # elif self.joy_info.buttons[6]:  # 'back' button
        #     # print('stop')
        #     self.joystick_started = False


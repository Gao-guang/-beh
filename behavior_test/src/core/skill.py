import rospy
from btree.core import Leaf, Status
from math import atan2, radians, fabs



class Skill(Leaf):
    """
    Skill node to execute special skill.
    """

    def __init__(self, bb):
        """
        Initialize skill.

        :param bb: blackboard from behavior tree
        :type bb: DBlackboard
        """
        super(Skill, self).__init__()

    @property
    def bb(self):
        """
        Returns the dblackboard of this task.

        :return: the blackboard
        :rtype: DBlackboard
        """
        return super(Skill, self).get_bb()

    def do(self, cmd):
        """
        Do given body command.

        :param cmd: given body command
        :type cmd: BodyCommand
        """
        self.bb.action_cmd.bodyCmd = cmd

    def walk(self, forward=0, left=0, turn=0):
        """
        Let robot walk with given parameters.

        :param forward: distance (cm) to walk forward by single step
        :type forward: float
        :param left: distance (cm) to walk leftward by single step
        :type left: float
        :param turn: angle (in degree) to turn around
        :type turn: float
        """

    def crouch(self):
        """
        Let robot crouch.
        """

    def stand(self):
        """
        Let robot stand straight.
        """


    def running(self):
        if self.bb.param.print_routes:
            self.print_running_route('Running')
        super(Skill, self).running()

    def success(self):
        super(Skill, self).success()

    def failure(self):
        if self.bb.param.print_routes:
            self.print_running_route('Failure')
        super(Skill, self).failure()

    def print_running_route(self, status):
        running_route = '{}: {}'.format(status,
                                        self.get_tree().get_running_route())
        # self.bb.behavior_info.running_route += '{}\n'.format(running_route)
        rospy.loginfo(running_route)


class Do(Skill):
    """
    Do simple action command.
    """

    def __init__(self, bb, cmd='crouch'):
        super(Do, self).__init__(bb)
        self.cmd = cmd

    def execute(self):
        if self.cmd == 'crouch':
            self.crouch()
        elif self.cmd == 'step':
            self.step()
        elif self.cmd == 'stand':
            self.stand()
        elif self.cmd == 'head_up':
            self.look_at(0, 0)
        elif self.cmd == 'back':
            self.backward()
        else:
            self.crouch()
        return Status.SUCCEEDED


class Complain(Skill):
    """
    Complain some messages
    """

    def __init__(self, bb, msg):
        super(Complain, self).__init__(bb)
        self.msg = msg

    def execute(self):
        rospy.logwarn(self.msg)
        return Status.SUCCEEDED

from dbehavior.btree.leaf import ConditionLeaf
from dbehavior.util.mathutil import get_magnitude
from dbehavior.util import VecPos
from math import fabs
import rospy


class IsFarStair(ConditionLeaf):
    def condition(self, d):
        rospy.logwarn('stair_distance: {}'.format(self.get_bb().vision_info.stair_distance))
        if self.get_bb().vision_info.stair_distance > d:
            rospy.logwarn('IsFar  d: {}'.format(d))
            return True

        rospy.logwarn('NotFar  d: {}'.format(d))
        return False

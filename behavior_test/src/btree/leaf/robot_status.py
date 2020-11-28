from dbehavior.btree.leaf import ConditionLeaf
from dbehavior.util.mathutil import get_dis, abs_angle_diff
from dbehavior.util import VecPos, Timer


class Kicking(ConditionLeaf):

    def condition(self):
        return self.get_bb().kicking


class LowerBoardReconnected(ConditionLeaf):

    def condition(self):
        return self.get_bb().timer_lower_board_reconnected.elapsed() <= \
               self.get_bb().param.motion_init_time


class IMUInitialized(ConditionLeaf):

    def condition(self):
        return self.get_bb().param.motion_init_time <= self.get_bb().timer_lower_board_reconnected.elapsed() <= \
               self.get_bb().param.motion_init_time + 30  # for new picking rule


class ReEntrying(ConditionLeaf):

    def condition(self):
        # 15s for Fast ReEntry
        return self.get_bb().timer_lower_board_reconnected.elapsed() <= \
               self.get_bb().param.motion_init_time + 15


class ReEntryLocalization(ConditionLeaf):

    def condition(self):
        return self.get_bb().param.motion_init_time + 5 <= self.get_bb().timer_re_entry.elapsed() <= \
               self.get_bb().param.motion_init_time + 10


class ReEntryOccurred(ConditionLeaf):

    def condition(self):
        return self.get_bb().timer_re_entry.elapsed() <= \
               self.get_bb().param.motion_init_time + 25


class MotionReStable(ConditionLeaf):

    def condition(self):
        return self.get_bb().timer_motion_re_stable.elapsed() <= 3


class GotPos(ConditionLeaf):

    def __init__(self, dst, dis_tol=20, angle_tol=10):
        super(GotPos, self).__init__()
        self.dst = dst
        self.dis_tol = dis_tol
        self.angle_tol = angle_tol

    def condition(self):
        robot_pos = VecPos.from_vector3(self.get_bb().vision_info.robot_pos)

        dis = get_dis(self.dst, robot_pos)
        diff_angle = abs_angle_diff(self.dst.z - robot_pos.z)

        return dis < self.dis_tol and diff_angle < self.angle_tol


class GotOutOfPos(ConditionLeaf):

    def __init__(self, dst, dis_tol=20, angle_tol=10):
        super(GotOutOfPos, self).__init__()
        self.dst = dst
        self.dis_tol = dis_tol
        self.angle_tol = angle_tol

    def condition(self):
        robot_pos = VecPos.from_vector3(self.get_bb().vision_info.robot_pos)
        dis = get_dis(self.dst, robot_pos)
        diff_angle = abs_angle_diff(self.dst.z - robot_pos.z)

        return dis >= self.dis_tol and diff_angle >= self.angle_tol


class GotInitPos(ConditionLeaf):

    def __init__(self, dis_tol=30, angle_tol=15):
        super(GotInitPos, self).__init__()
        self.dis_tol = dis_tol
        self.angle_tol = angle_tol

    def condition(self):
        dst = self.get_bb().init_pos
        robot_pos = VecPos.from_vector3(self.get_bb().vision_info.robot_pos)
        dis = get_dis(dst, robot_pos)
        diff_angle = abs_angle_diff(dst.z - robot_pos.z)

        return dis < self.dis_tol and diff_angle < self.angle_tol


class GotOutOfInitPos(ConditionLeaf):

    def __init__(self, dis_tol=50, angle_tol=20):
        super(GotOutOfInitPos, self).__init__()
        self.dis_tol = dis_tol
        self.angle_tol = angle_tol

    def condition(self):
        dst = self.get_bb().init_pos
        robot_pos = VecPos.from_vector3(self.get_bb().vision_info.robot_pos)
        dis = get_dis(dst, robot_pos)
        diff_angle = abs_angle_diff(dst.z - robot_pos.z)

        initial_entry_exit = dis >= self.dis_tol and diff_angle >= self.angle_tol
        in_enemy_field = (self.get_bb().param.attack_right and robot_pos.x > 10) or \
                         (not self.get_bb().param.attack_right and robot_pos.x < -10)
        return initial_entry_exit or in_enemy_field


class KickEnabled(ConditionLeaf):

    def condition(self):
        print("kick: ", self.get_bb().timer_kick_success.elapsed())
        return self.get_bb(
        ).kick_enabled  # and self.get_bb().timer_kick_success.elapsed() > 3


class AttackRight(ConditionLeaf):

    def condition(self):
        return self.get_bb().param.attack_right


class AttackLeft(ConditionLeaf):

    def condition(self):
        return not self.get_bb().param.attack_right


class KickSuccess(ConditionLeaf):

    def condition(self):
        return 0 <= self.get_bb().timer_kick_success.elapsed() <= 7


class JoystickStarted(ConditionLeaf):

    def condition(self):
        return self.get_bb().joystick_started


class JoystickStopped(ConditionLeaf):

    def condition(self):
        return not self.get_bb().joystick_started


class JoystickEntryOccurred(ConditionLeaf):

    def condition(self):
        return 10 <= self.get_bb().timer_joystick_started.elapsed() <= 25


class FarFromInitPos(ConditionLeaf):

    def __init__(self, dis_tol=350, angle_tol=90):
        super(FarFromInitPos, self).__init__()
        self.dis_tol = dis_tol
        self.angle_tol = angle_tol

    def condition(self):
        dst = self.get_bb().init_pos
        robot_pos = VecPos.from_vector3(self.get_bb().vision_info.robot_pos)
        dis = get_dis(dst, robot_pos)
        diff_angle = abs_angle_diff(dst.z - robot_pos.z)
        if self.get_bb().param.attack_right:
            in_enemy_field = robot_pos.x >= 10
        else:
            in_enemy_field = robot_pos.x <= -10

        return dis >= self.dis_tol and \
               diff_angle <= self.angle_tol and \
               in_enemy_field


class NearCornerZone(ConditionLeaf):

    def __init__(self, tol=20):
        super(NearCornerZone, self).__init__()
        self.tol = tol
        self.timer = Timer()

    def condition(self):
        robot_pos = VecPos.from_vector3(self.get_bb().vision_info.robot_pos)
        field_length = self.get_bb().param.field_length
        goal_depth = self.get_bb().param.goal_depth
        goal_area_length = self.get_bb().param.field_length
        if self.get_bb().param.attack_right:
            near_corner_zone = -field_length - goal_depth - self.tol <= robot_pos.x <= -field_length + goal_area_length + self.tol
        else:
            near_corner_zone = field_length + goal_depth + self.tol >= robot_pos.x >= field_length - goal_area_length - self.tol
        if not near_corner_zone:
            self.timer.restart()
        return near_corner_zone

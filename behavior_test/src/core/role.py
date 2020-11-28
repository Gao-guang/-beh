from btree.core import BehaviorTree
from skill import Do

class Role(BehaviorTree):

    """
    Role for robot to act in the playground.
    """
    def __init__(self, bb):
        super(Role, self).__init__(bb)
        self.root = Do(bb)
        self.add_child(self.root)

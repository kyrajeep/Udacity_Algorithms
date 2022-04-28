# f = g + h where h is a heuristic (estimated cost to goal)
#and g is the distance from current node


class a_star:
    def __init__(root, goal, graph):
        self.root = root
        self.left = None
        self.right = None
        self.open_list = list()
        self.closed_list = list()
        self.cur_node = root
    def a_star():
        #bring it all together
        pass
    def heuristic(cur_node):
        # use Pythagorean Theorem
        return h
    def children(cur_node):
        # generate children of the current node
        left = cur_node.left
        right = cur_node.right
        return left, right
    def distance():
        # calculate how far away a node is from current
        pass

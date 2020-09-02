# Given a group with subgroups and users represented
# as string ID's write a function to check if a 
# user is in the group.
# Each group is like a node and is the user in the node?

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
        if user in group.users:
            return True
        group_list = group.groups
        group_len = len(group_list)

        for i in range(group_len):
            result = is_user_in_group(user, group_list[i])
            if result == True:
                return True
 
    

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
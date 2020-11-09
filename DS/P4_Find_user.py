# Given a group with subgroups and users represented
# as string ID's write a function to check if a 
# user is in the group.
# note to self: Each group is like a node and is the user in the node?

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
        # reminder: if you need to access an attribute 
        # of a class you can always write a getter! :D
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    
    #Return True if user is in the group, False otherwise.

    #Args:
     # user(str): user name/id
      #group(class:Group): group to check user membership against
    # base case    
    if user in group.get_users():
        return True
        
    group_list = group.get_groups()
    group_len = len(group_list)
    # recursive call for each subgroup
    for i in range(group_len):
        result = is_user_in_group(user, group_list[i])
        if result == True:
            return True
    return False
    
#Test Case 1: one subgroup per supergroup with one user each

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_user('hello_user')
child.add_group(sub_child)
parent.add_group(child)

# Expected Values: True
print(is_user_in_group("sub_child_user", parent))
print(is_user_in_group("hello_user", parent))
# # Expected Value: False

print(is_user_in_group("hello_user", sub_child))

# Test Case 2

Mammals = Group("Mammals")
Felines = Group("Felines")
Lions = Group("Lions")
Cats = Group("Cats")
Dogs = Group("Dogs")

# Mammals have subgroups Cats, Dogs, and Lions
Mammals.add_group(Cats)
Mammals.add_group(Lions)
Felines.add_group(Cats)
Felines.add_group(Lions)

Lions.add_user("Simba")
Cats.add_user("Orie")
Cats.add_user("Effie")
Cats.add_user("Immi")

# Expected Value: True
print(is_user_in_group("Immi", Mammals))
# False
print(is_user_in_group("Immi", Lions))
# True
print(is_user_in_group("Orie", Mammals))
# False. Checks if an empty subgroup is ok
print(is_user_in_group("Orie", Dogs))


#Test Case 3: the group is empty
Horses = Group("Horses")
# Expected Value: False
print(is_user_in_group("Orie", Horses))

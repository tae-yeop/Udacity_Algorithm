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
    
    def __repr__(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    group_list = group.get_groups()
    user_list = group.get_users()
  
    if user in user_list:
        return True
    else:
        for sub_group in group_list:
            return is_user_in_group(user, sub_group)
#     print(f'{user} , {group}')
    return False


# Test case 1
print('Test case 1')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent)) # True

# Test case 2
print('Test case 2')
parent = Group("parent")
parent.add_user("parent_1")
parent.add_user("parent_2")
parent.add_user("parent_3")

print(is_user_in_group("parent_1", parent)) # True
print(is_user_in_group("parent_2", parent)) # True
print(is_user_in_group("parent_3", parent)) # True
print(is_user_in_group("parent_4", parent)) # False

# Test case 3
print('Test case 3')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
sub_child_user = "sub_child_user"
child_user = "child_user"

parent.add_user(parent_user)
child.add_user(child_user)
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent)) # True
print(is_user_in_group("sub_child_user", child)) # True
print(is_user_in_group("sub_child_user", sub_child)) # True

print(is_user_in_group(child_user, parent)) # True
print(is_user_in_group(child_user, child)) # True
print(is_user_in_group(child_user, sub_child)) # False

print(is_user_in_group(parent_user, parent)) # True
print(is_user_in_group(parent_user, child)) # False
print(is_user_in_group(parent_user, sub_child)) # False

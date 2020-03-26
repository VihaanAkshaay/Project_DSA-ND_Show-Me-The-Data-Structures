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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():  # User found
        return True
    else:
        if len(group.get_groups()) == 0:  # Keep searching
            return False
        else:
            for sub_group in group.get_groups():
                found = is_user_in_group(user, sub_group)

                if found:
                    return True
    return False

parent = Group("parent")
parent_user = "parent_user"
parent.add_user(parent_user)

child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group(sub_child_user, parent))
# expected output: True
print("Pass" if is_user_in_group(sub_child_user, parent)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group(sub_child_user, child))
# expected output: True
print("Pass" if is_user_in_group(sub_child_user, child)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group(parent_user, parent))
# expected output: True
print("Pass" if is_user_in_group(parent_user, parent)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group(parent_user, child))
# expected output: False
print("Pass" if is_user_in_group(parent_user, child)== False else "Fail")
print('------------------------------------------')

print(is_user_in_group("sub_child_user", parent))
# expected output: True
print("Pass" if is_user_in_group("sub_child_user", parent)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group("super_user", parent))
# expected output: False
print("Pass" if is_user_in_group("super_user", parent)== False else "Fail")
print('------------------------------------------')


print(is_user_in_group(None, parent))
# expected output: False
print("Pass" if is_user_in_group(None, parent)== False else "Fail")
print('------------------------------------------')



empty_group = Group("emptygroup")

print(is_user_in_group(None, empty_group))
# expected output: False
print("Pass" if is_user_in_group(None, empty_group)== False else "Fail")
print('------------------------------------------')


print(is_user_in_group("User", empty_group))
# expected output: False
print("Pass" if is_user_in_group("User", empty_group)== False else "Fail")
print('------------------------------------------')


#%% Some more test cases
# Testing preparation
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Normal Cases:
print('Normal Cases:')
print(is_user_in_group(user='parent_user', group=parent))
# False
print(is_user_in_group(user='child_user', group=parent))
# False
print(is_user_in_group(user='sub_child_user', group=parent), '\n')
# True

# Edge Cases:
print('Edge Cases:')
print(is_user_in_group(user='', group=parent))
# False
print(is_user_in_group(user='', group=child))
# False
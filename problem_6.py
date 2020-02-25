class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union = set()
    current_node = llist_1.head
    while current_node:
        union.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        union.add(current_node.value)
        current_node = current_node.next


    union_head = Node(None)
    union_current = union_head
    for element in union:
        union_current.next = Node(element)
        union_current = union_current.next
    union_head = union_head.next
    union_list = LinkedList()
    union_list.head = union_head
    return union_list

def intersection(llist_1, llist_2):

    values_set1 = set()
    current_node = llist_1.head
    while current_node:
        values_set1.add(current_node.value)
        current_node = current_node.next

    values_set2 = set()
    current_node = llist_2.head
    while current_node:
        values_set2.add(current_node.value)
        current_node = current_node.next

    intersection_head = Node(None)
    intersection_current_node = intersection_head
    intersection_set = values_set1.intersection(values_set2)
    for element in intersection_set:
        intersection_current_node.next = Node(element)
        intersection_current_node = intersection_current_node.next
    intersection_head = intersection_head.next

    intersection_list = LinkedList()
    intersection_list.head = intersection_head

    return intersection_list

    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
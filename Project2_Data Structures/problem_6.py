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
        out_string += "End"
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
    head_1 = llist_1.head
    head_2 = llist_2.head
    
    union_ll = LinkedList()
    union = set()

    while head_1:
        union.add(head_1.value)
        head_1 = head_1.next
    while head_2:
        union.add(head_2.value)
        head_2 = head_2.next
        
    for i in union:
        union_ll.append(i)

    return union_ll

def intersection(llist_1, llist_2):
    # Your Solution Here
    head_1 = llist_1.head
    head_2 = llist_2.head
    
    value_dict = dict()
    intersection_ll = LinkedList()

    while head_1:
        value_dict.setdefault(head_1.value, 0)
        head_1 = head_1.next

    while head_2:
        if value_dict.setdefault(head_2.value, 1) == 0:
            value_dict[head_2.value] = 2
        head_2 = head_2.next

    for k, v in value_dict.items():
        if v == 2:
            intersection_ll.append(k)

    return intersection_ll

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print (union(linked_list_1,linked_list_2)) # {32, 65, 2, 3, 4, 35, 6, 1, 9, 11, 21}
print (intersection(linked_list_1,linked_list_2)) # {4, 6, 21}

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # {1,2,3,4,6,7,8,9,11,21,23,35,65}
print (intersection(linked_list_3,linked_list_4)) # {None}


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [0, 100]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6)) # {0, 100}
print (intersection(linked_list_5,linked_list_6)) # {None}
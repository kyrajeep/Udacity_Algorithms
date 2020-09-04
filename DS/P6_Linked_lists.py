class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, value):
        # this function is from Udacity template
        # travel to the last node (repeat going to the next
        # until you run out.)
        
        if self.head is None:
            self.head = Node(value)
            

        else:
            cur_node = Node(value)
            node = self.head
            while node:
                if node.next:
                    node = node.next
                else:
                    node.next = cur_node
                    return
        
def iter_onelist(l1, all_element):
    node = l1.head
    not_inter = []
    if all_element == {}:
        while node:
        
            a = node.value
            all_element[a] = 1
            
            node = node.next
        return all_element
    else: 
        while node:
            
            a = node.value
            if a in all_element.keys():
                if a not in not_inter: 
                    all_element[a] += 1
            else:
                all_element[a] = 1
                not_inter.append(a)
            
            node = node.next
        return all_element
def iter_list(l1, l2):
    
    pass_in = iter_onelist(l1, {})
    all_element=iter_onelist(l2, pass_in)
    print(all_element) 
    return all_element
def intersection(l1, l2):
    #input: two linked lists
    #output: a linked list with elements in intersection
    inter_l = []
    all_element = iter_list(l1, l2)
    for i in all_element.keys():
        if all_element[i] > 1:
            
            inter_l.append(i)
    return inter_l

# Test case 1 & 2 taken from Udacity template and modified
# Test case 1
def union(l1, l2):
    union_l = []
    all_element = iter_list(l1, l2)
    for i in all_element.keys():
        union_l.append(i)
    return union_l

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
# create linked lists for the input from lists
# elements repeated in the list but not in another are not eligible
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    try:
        linked_list_1.add_node(i)
        
    except:
        print("an error occured")

for i in element_2:
    try:
        linked_list_2.add_node(i)
        
    except:
        print("an error occured")


# Expected output = [4, 6, 21]
print (intersection(linked_list_1,linked_list_2))
# Expected output = [3,2,4,35,6,65,32,9,1,11,21]
print (union(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,65,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.add_node(i)

for i in element_2:
    linked_list_4.add_node(i)

#print (union(linked_list_3,linked_list_4))
#print (intersection(linked_list_3,linked_list_4))

# Test Case 3 
# Is there an edge case for this problem?
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1]
element_2 = [2, 1]

for i in element_1:
    linked_list_5.add_node(i)

for i in element_2:
    linked_list_6.add_node(i)

#print (union(linked_list_5,linked_list_6))
#print (intersection(linked_list_5,linked_list_6))

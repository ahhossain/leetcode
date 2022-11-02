class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def remove_from_tail(self):
        if self.head == None:
            return
        for current_node in self:
            if current_node.next.next == None:
                temp = current_node.next
                current_node.next = None
                return temp

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return " -> ".join(nodes)

def mergeTwoLists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged = LinkedList()
    node1 = list1.head
    node2 = list2.head
    while node1 != None and node2 != None:
        if node1.val < node2.val:
            merged.add_to_tail(Node(node1.val))
            node1 = node1.next

        if node2.val < node1.val:
            merged.add_to_tail(Node(node2.val))
            node2 = node2.next

        if node1.val == node2.val:
            merged.add_to_tail(Node(node1.val))
            node1 = node1.next
            merged.add_to_tail(Node(node2.val))
            node2 = node2.next

    return merged

ll1 = LinkedList()
ll2 = LinkedList()

#ll1.add_to_tail(Node(1))
#ll1.add_to_tail(Node(2))
#ll1.add_to_tail(Node(4))

ll2.add_to_tail(Node(0))
#ll2.add_to_tail(Node(3))
#ll2.add_to_tail(Node(4))

print(ll1)
print(ll2)

print(mergeTwoLists(ll1, ll2))

#print("ll:", ll1)
#first = ll1.remove_from_head()
#print("removed:", first)
#print("ll:", ll1)
#last = ll1.remove_from_tail()
#print("removed:", last)
#print("ll:", ll1)
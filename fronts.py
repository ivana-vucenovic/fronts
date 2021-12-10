
class Node:
    def __init__(self, val):
        self.val = val 
        self.next= None 

class SLL:
    def __init__(self):
        self.head = None

# Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

    def addFront(self, val):
        new_node = Node(val)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node
        return self

# Write a method to remove the head node and return the new list head node. If the list is empty, return null.

    def removeFront(self):
        if self.head == None:
            return None
        self.head = self.head.next
        return self.head

# Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.

    def front(self):
        if self.head == None:
            return None
        return self.head.val


sll = SLL()
sll.addFront("Francesco")
sll.addFront("Maria")

sll.removeFront()

sll.front()

print(sll.head.val)



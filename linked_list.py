# creating a class node- 
# begin by keyword 'Class' and class name, after the you put a  :
# then define a function, write a constructor

class Node:
     def __init__(self,data):
          self.info = data
          self.next = None

# creating an object from class node- 
# first srtart with the class name then the name ofthe object , -
# pass required parameters
one = Node(1)
two = Node(2)
three = Node(3)

#printing
#print(one) - shows a memory address where an object hs been stored


#linking a list
one.next = two
two.next = three

#print
print(one.next)
print(two)
print(three.next)



class singlyLinkedList:
     def __init__(self):
        self.head = None
     def insertAtFront(self, data):
          newNode = Node(data)
          newNode.next = self.head
          self.head = newNode

     def traverse(self):
          start = self.head
          while start:     # if start has a value the loop continues
               print(start.info)
               start = start.next  # assignment create an object outside this class


#object
llist = singlyLinkedList()

llist.insertAtFront(1)
llist.insertAtFront(2)
llist.insertAtFront(3)
llist.traverse()
               

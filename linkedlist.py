class Node:
  def __init__(self,data= None,next = None):
    self.data = data
    self.next = next

class LinkedList:
    """This is a linked list implementation"""
    def __init__(self):
      self.head = None 
      
    def push_front(self, val):
        """Add a new element to the front of the linked list. O(1)"""
        if self.head is None:
           self.head = Node(val,None)
           return
        
        new_node = Node(val,self.head)
  
        self.head = new_node 
        

    def get_element(self, index):
        """Returns the value of the element at the provided index. O(n)"""
        if index >= self.count():
          raise Exception (" Index out of range ")
        itr = self.head
        count = 0
        while itr:
          if count == index:
            return itr.data
          itr = itr.next  
          count += 1  
        return None

    def count(self):
        """Returns the number of elements in the list. O(1)"""
        count = 0
        itr = self.head 
        while itr:
           count += 1 
           itr = itr.next
        return count   
        

    def pop_front(self):
        """Removes the element from the front of the list and returns the value
        of that element. O(1)"""
        if self.head is not None:
          removed_value = self.head.data
          self.head = self.head.next
          return removed_value
        else:
          print( "empty list")
          return None
        

    def insert_after(self, index, val):
        """Inserts an element in the list after the provided index. O(n)"""
        new_node = Node(val)
        current = self.head
        position = 0
        while current :
          if position == index:
            new_node.next = current.next
            current.next = new_node
            return
          position +=1
          current = current.next 
        print("index not found")
        
    def remove_element(self, index):
        """Removes element at the provided index. Returns the removed
        element's value. O(n)"""
        if index < 0 :
           print("invalid index ")
        if index == 0 :
          if self.head is not None:
            self.head = self.head.next
            return
          else:
            print( "empty list")
            return
        current = self.head
        position = 0
        while current:
          if position == index -1:
           if current.next is not None:
             current.next = current.next.next
             return
           else:
             print( "index is out of list ")
          current = current.next
          position += 1
             
        print("index not found")
          
         

    def reverse(self):
        """Reverses the direction of the linked list. O(n)""" 
        prev = None
        current = self.head
        while current:
          next_node = current.next
          current.next = prev
          prev = current
          current = next_node

        self.head = prev
          
    

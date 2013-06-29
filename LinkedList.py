class List:
    """
    Implementation of a Singely Linked List.
    """
    def __init__(self):
        """ (List) -> NoneType
        Initialize the head and tail of the list
        """
        self.head = None
        self.tail = None

    def __str__(self):
        """ (List) -> str
        
        """
        result = ''
        node_counter = 0
        node = self.head
        while node != None:
            result = 'Node ' + str(node_counter) + ': ' + str(node.data) + '\n'
            node = node.next
            node_counter += 1
        return result

    def is_empty(self):
        """ (List) -> bool
        Checks to see if the head of the list is a reference to none.
        """
        return self.head == None

    def insert(self, node, data=None):
        """ (List, ListNode, Object) -> NoneType

        Creates and inserts a new node AFTER an existing node, updating the tail
        when inserted at the end.
        """
        new_node = ListNode(data, node.next)
        node.next = new_node
        if self.tail == node:
            self.tail = new_node

    def insert_end(self, data):
        """ (List, Object) -> NoneType

        Insert the node at the end of the List.
        """
        # Check if the list is empty
        if self.tail == None:
            new_node = ListNode(data, None)
            self.head = self.tail = new_node # The new node is both head and tail
        else:
            self.insert(self.tail, data)

    def insert_beginning(self, data):
        """ (List, Object) -> NoneType

        Insert Node at the beginning of the List.
        """
        new_node = ListNode(data, self.head)
        self.head = new_node

    def add(self, data):
        """ (List, Object) -> NoneType
        Simplier name than insert_beginning.
        """
       self.insert_beginning(data) 
        
    def remove_after(self, node):
        """ (List, ListNode) -> NoneType

        Remove the node after the specified node.
        """
        node.next = node.next.next
        if node.next == None:
            self.tail = node
            
    def remove_beginning(self):
        """ (List) -> NoneType

        Remove the first node in the List.
        """
        self.head = self.head.next
        if self.head == None:
            self.tail = None

    def length(self):
        """ (List) -> int

        Return the number of items in the list.
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count


    def find_first(self, data):
        """ (List, Object) -> ListNode

        Finds the first occurance of the specified data in the list and returns the node.
        If data is not in the list, will return None.
        """
        find_first_func(lambda x: x == data)

    def find_first_func(self, func):
        """ (List, Function) -> Node

        User supplies a predicate (function returning a boolean) and returns the first
        node for which it returns True.
        
        >>> node = list.find_first_func(lambda x: 2*x + 7 == 19)
        """
        node = list.head
        while node != None:
            if func(node.data):
                return node
            node = node.next
        

class ListNode:
    """
    The basic building block for a linked list data structure.
    """

    def __init__(self, new_data, new_next = None):
        """ (Node, Object, ListNode) -> NoneType

        Initialize the Node with the data. Assumes the Node doesn't point to
        any Node to start.

        Nodes should only point to another ListNone, or to None if there isn't one.
        """
        self.data = new_data
        self.next = new_next

    def get_data(self):
        """ (ListNode) -> Object
        
        Return the data in the Node.
        """
        return self.data

    def get_next(self):
        """ (ListNode) -> ListNode
    
        Return the Node which the current node points to. This is the next node in the list.
        """
        return self.next

    def set_data(self, new_data):
        """ (ListNode, Object) -> NoneType
        
        Set the data inside the Node
        """
        self.data = new_data

    def set_next(self, new_next):
        """ (ListNode, Object) -> NoneType
        
        Set a Node for which the current Node will now point to.
        """
        self.next = new_next

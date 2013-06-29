class UnorderedList:
    """
    """

class Node:
    """
    The basic building block for a linked list data structure.
    """

    def __init__(self, init_data):
        """ (Node, Object) -> NoneType

        Initialize the Node with the data. Assumes the Node doesn't point to
        any Node to start.
        """
        self.data = init_data
        self.next = None

    def get_data(self):
        """
        Return the data in the Node.
        """
        return self.data

    def get_next(self):
        """
        Return the Node which the current node points to
        """
        return self.next

    def set_data(self, new_data):
        """
        Set the data inside the Node
        """
        self.data = new_data

    def set_next(self, new_next):
        """
        Set a Node for which the current Node will now point to.
        """
        self.next = next

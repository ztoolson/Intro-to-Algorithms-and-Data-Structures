class Queue:
    """
    
    """

    def __init__(self):
        """ (Queue) -> NoneType

        Initializes an empty queue.
        """
        self.items = []

    def isEmpty(self):
        """ (Queue) -> bool

        Returns True if there are no items in the queue.
        """
        return self.items == []

    def enqueue(self, item):
        """ (Queue, Object) -> NoneType

        Adds the items to the queue. This places is it at the front of the list.
        O(n) time.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """ (Queue) -> Object

        Removes the last item in the list.
        O(1)
        """
        return self.items.pop()

    def size(self):
        """ (Queue) -> int

        Returns the number of items in the Queue.
        """
        return len(self.items)


if __name__ == '__main__':

    def hot_potato(name_list, num):
        """ (list, int) -> str

        This is a general simulation of the game hot potato. In this game children
        line up in a circle and pass an item from neightbor to neighbor as fast as they
        can. At a certain point in the game, the action is stopped and the child who has the
        item is removes from the game. Play continues until only one child is left.

        This method returns who is left with the condition that the potato will be passed
        num times.

        >>> hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)
        'Susan'
        """
        sim_queue = Queue()

        for name in name_list:
            sim_queue.enqueue(name)

        # Move the person at the front of the list to the end of the list num times.
        while sim_queue.size() > 1:
            for i in range(num):
                sim_queue.enqueue(sim_queue.dequeue())
            sim_queue.dequeue()

        return sim_queue.dequeue()
    

        

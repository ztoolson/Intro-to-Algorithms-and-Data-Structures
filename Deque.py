class Deque:
    """
    Implements a double ended Queue.
    """

    def __init__(self):
        """ (Deque) -> NoneType

        Initializes an implementation of a deque using a list.
        """
        self.items = []

    def is_empty(self):
        """ (Deque) -> bool

        Returns True of there are no items in the deque.
        """
        return self.items == []

    def add_front(self, item):
        """ (Deque) -> NoneType

        Adds item to the front of the deque
        O(1)
        """
        self.items.append(item)

    def add_rear(self, item):
        """ (Deque) -> NoneType

        Adds items to the rear of the deque.
        O(n)
        """
        self.items.insert(0, item)

    def remove_front(self):
        """ (Deque) -> Object

        Removes and returns the item at the front of the deque.
        O(1)
        """
        return self.items.pop()

    def remove_rear(self):
        """ (Deque) -> Object

        Removes and returns the item at the rear of the deque.
        O(n)
        """
        return self.items.pop(0)

    def peek_front(self):
        """ (Deque) -> Object

        Returns the item at the front of the deque. Does not remove from the deque.
        """
        return self.items[-1]
    
    def peek_rear(self):
        """ Deque) -> Object

        Returns the item at the rear of the deque. Does not remove from the deque.
        """
        return self.items[0]

    def size(self):
        """ (Deque) -> int
        """
        return len(self.items)


if __name__ == '__main__':

# Using a deque to see if a string is a palindrome.

    def is_palindrome(str):
        """

        >>> is_palindrome('lsdkjfskf')
        False
        >>> is_palindrome('radar')
        True
        """
        char_deque = Deque()

        # Poplate the deque with each char in str
        for ch in str:
            char_deque.add_front(ch)

        still_equal = True

        # Remove item from front and rear of deque, and compare them.
        # If at anytime the two items are not equal, will mark still_equal to False.
        while char_deque.size() > 1 and still_equal:
            first = char_deque.remove_front()
            last = char_deque.remove_rear()
            if first != last:
                still_equal = False

        return still_equal

import random

class Task:
    """
    This is a class that will be sent to the printer.
    """
    def __init__(self, time):
        """ (Task, int) -> None

        Initializes that Task and gives it a timestamp and a random number of
        pages between 1 - 20.
        """
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        """ (Task) -> int

        Returns the time stamp of the Task.
        """
        return self.timestamp

    def get_pages(self):
        """ (Task) -> int)

        Returns the number of pages the Task has.
        """
        return self.pages

    def wait_time(self, currenttime):
        """ (Task, int)

        Returns the time the task has been waiting.
        """
        return currenttime - self.timestamp

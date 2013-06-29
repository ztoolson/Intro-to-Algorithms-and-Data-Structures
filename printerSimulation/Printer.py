class Printer:
    """
    This represents the printer in a students classroom.
    """
    def __init__(self, ppm):
        """ (Printer, int) -> None

        Initialize the printer. Printer must know the printing rate, the current task,
        and the tim remaining on the task
        """
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """ (Printer) -> None

        Printer does one second of printing.
        """
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        """ (Printer) -> bool

        Returns True if the printer is currently printing a task.
        """
        return self.current_task != None
            

    def start_next(self, newtask):
        """ (Printer, Task) -> None

        Updates the printers current_task and the time_remaining on the task.
        """
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * (60/self.page_rate) #UNITS: pages * page per second

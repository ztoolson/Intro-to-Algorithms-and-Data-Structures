import random
import Queue
import Printer
import Task

def simulation(num_seconds, pages_per_minute):
    """ (int, int) -> None
    Problem:
    On any average day about 10 students are working in the lab at
    any given hour. These students typically print up to twice during
    that time, and the length of these tasks ranges from 1 to 20 pages.
    The printer in the lab is older, capable of processing 10 pages per
    minute of draft quality. The printer could be switched to give
    better quality, but then it would produce only five pages per minute.
    The slower printing speed could make students wait too long.
    What page rate should be used?
    """

    labprinter = Printer.Printer(pages_per_minute)
    print_queue = Queue.Queue()
    waitingtimes = []

    for current_second in range(num_seconds):
        
        # Does a new print task get created?
        if new_print_task():
            # If a new task is created, add it to the queue with the current second as timestamp
            task = Task.Task(current_second)
            print_queue.enqueue(task)

        # Printer is not busy and a Task is waiting
        if (not labprinter.busy()) and (not print_queue.isEmpty()):
            # remoce the next task from the print queue and assign it to the printer
            nexttask = print_queue.dequeue()
            # Computer waiting time for nexttask
            waitingtimes.append(nexttask.wait_time(current_second))
            labprinter.start_next(nexttask)

        # Printer does one second of printing
        labprinter.tick()

    average_wait= sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait,print_queue.size()))


def new_print_task():
    """ (None) -> bool

    Returns True if a task is created. If there are 10 students in the lab and
    each prints twice, then there are 20 print tasks per hours on average. 20 tasks
    per hour means on average there will be one task every 180 seconds. A Task is then
    created in this method if a random number from 1 - 180 inclusive == 180.

    """
    num = random.randrange(1,181)
    return num == 180
        

# Runs the simulation    
if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)

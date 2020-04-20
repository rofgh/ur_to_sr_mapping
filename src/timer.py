
from timeit import default_timer as timer

def start():
    start = timer()
    return start

def end(start):
    end = timer()
    total_time = end - start
    time_elapsed = "Total for this run: {tt:.2} seconds\n"
    print(time_elapsed.format(tt=total_time))
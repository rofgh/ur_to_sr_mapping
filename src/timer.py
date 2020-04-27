
from timeit import default_timer as timer

def start():
    start = timer()
    return start

def end(start):
    end = timer()
    total_time = end - start
    time_elapsed = "Total for this run: {tt} seconds\n"
    if total_time > 60:
        total_time = total_time/60
        time_elapsed = "Total for this run: {tt:.5} minutes\n"
    print(time_elapsed.format(tt=total_time))
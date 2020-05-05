
from timeit import default_timer as timer

def start():
    start           = timer()
    return start

def check(start, then, iters):
    now             = timer()
    elapsed         = now - start
    one_lang        = now - then
    average         = elapsed/iters
    time_elapsed    = "Elapsed time since start:\t {tt} seconds"
    if elapsed > 60:
        elapsed     = elapsed/60
        time_elapsed= "Elapsed time since start:\t {tt:.5} minutes"
    print(time_elapsed.format(tt=elapsed))
    lang_elapsed    = "Elapsed time for this language:\t {tt} seconds"
    print(lang_elapsed.format(tt=one_lang))
    average_time    = "Average time per language:\t {tt} seconds\n"
    print(average_time.format(tt=average))
    return now

def end(start):
    end             = timer()
    total_time      = end - start
    time_elapsed    = "Total for this run: {tt} seconds\n"
    if total_time > 60:
        total_time  = total_time/60
        time_elapsed= "Total for this run: {tt:.5} minutes\n"
    print(time_elapsed.format(tt=total_time))
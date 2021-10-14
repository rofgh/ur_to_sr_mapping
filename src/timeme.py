from timeit import default_timer as timer
from datetime import datetime


def start():
    start = timer()
    return start

def allowed_per_file(now):
    minutes_per_file    = 10  # minutes spent on each tsv file
    seconds_per_file    = minutes_per_file*60
    file_add            = now//seconds_per_file
    return file_add

def check(start, then, iters):
    now = timer()
    elapsed = now - start
    one_lang = now - then
    average = elapsed / iters
    time_elapsed = "Elapsed time since start:\t {tt:.5} seconds"
    if elapsed > 60:
        if elapsed > 3600:
            elapsed = elapsed / 3600
            time_elapsed = "Elapsed time since start:\t {tt:.5} hours"
        else:
            elapsed = elapsed / 60
            time_elapsed = "Elapsed time since start:\t {tt:.5} minutes"
    print(time_elapsed.format(tt=elapsed))
    lang_elapsed = "Elapsed time for this language:\t {tt:.5} seconds"
    print(lang_elapsed.format(tt=one_lang))
    average_time = "Average time per language:\t {tt:.5} seconds\n"
    print(average_time.format(tt=average))
    file_add = str(int(allowed_per_file(now)))
    return now, file_add


def end(start):
    end = timer()
    total_time = end - start
    time_elapsed = "Total for this run: {tt:.5} seconds"
    if total_time > 60:
        total_time = total_time / 60
        time_elapsed = "Total for this run: {tt:.5} minutes"
    # Also time of day
    time_of_day = "Ending at {tt}\n"
    print(time_elapsed.format(tt=total_time))
    print(time_of_day.format(tt=datetime.now()))

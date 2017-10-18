#!/usr/bin/env python3

# built-in modules
from datetime import datetime, timedelta
from pprint import pprint
import sched
import time
import argparse

# modules from packages
from pytz import timezone, utc
import pytz
from json_tricks.nonp import dump, load

s = sched.scheduler(time.time, time.sleep)


class TaskEntry(object):
    """
    An entry for a task to be tracked
    """

    def __init__(self, title, resetduration, lastreset=(datetime.min)):
        self.title = title
        self.resetduration = resetduration
        self.lastreset = lastreset


parser = argparse.ArgumentParser(
    description='Time since last checked and stuff.')
parser.add_argument('--reset_all', action='store_true',
                    help="mark all tasks complete at once to reset their timers.")
# TODO: error instead of silent failure if given an invalid task title
parser.add_argument('--reset', '-r', action='store', type=str,
                    help="mark a specific task complete, specified by title.")

args = parser.parse_args()

# Read the stuff from a file.
with open('tasks.json') as tasks_file:
    tasks = load(tasks_file)
    pprint(tasks)

cur_time = datetime.now()
print("\nCurrent time: " + str(cur_time))
# Print some info about all dat stuff in the file and update reset time
for task in tasks:
    if 'lastreset' not in task:  # in case we have a new task
        task['lastreset'] = datetime.min
    print("\n\n" + task['title'] + " " +
          str(task['resetduration']) + " " + str(task['lastreset']))
    print("\nTime since last completed:")
    print(cur_time - task['lastreset'])
    if (cur_time - task['lastreset']).days >= 1:
        print("Longer than 1 day since last run.")
    else:
        print("Not longer than 1 day since last run")
    if (cur_time - task['lastreset']) >= task['resetduration']:
        print("Longer than " + str(task['resetduration']) + " since last run.")
    else:
        print("Not longer than " +
              str(task['resetduration']) + " since last run.")
    if args.reset_all:
        print("Resetting all tasks.")
        task['lastreset'] = cur_time
    elif args.reset == task['title']:
        print("Resetting task " + task['title'])
        task['lastreset'] = cur_time


# Dump stuff back in the file
with open('tasks.json', 'w') as tasks_file:
    dump(tasks, tasks_file)

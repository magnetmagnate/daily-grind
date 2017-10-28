#!/usr/bin/env python3.6

# built-in modules
from datetime import datetime, timedelta
from pprint import pprint
import sched
import time
import argparse
import uuid

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
        self.id = uuid.uuid4().hex
        self.title = title
        self.resetduration = resetduration
        self.lastreset = lastreset


parser = argparse.ArgumentParser(
    description='Time since last checked and stuff.')
# if we get this argument, mark all tasks as completed
parser.add_argument('--reset_all', action='store_true')
parser.add_argument('--reset', help='Reset specific task by ID.')

args = parser.parse_args()

print("(Debug) Current arguments:")
pprint(args)

# Read the stuff from a file.
with open('tasks.json') as tasks_file:
    tasks = load(tasks_file)
    pprint(tasks)

# Set up some useful tracking variables and stuff.
cur_time = datetime.now()
task_reset = False

print("\nCurrent time: " + str(cur_time))
# Print some info about all dat stuff in the file and update reset time
for task in tasks:
    if not 'id' in task:
        print("ID for task does not exist, creating one.")
        task['id'] = uuid.uuid4().hex
    if 'lastreset' not in task:  # in case we have a new task
        task['lastreset'] = datetime.min
    print("\n\n" + task['title'] + " " +
          str(task['resetduration']) + " " + str(task['lastreset']))
    print("\nTime since last completed:")
    print(cur_time - task['lastreset'])
    if task['resetduration'] < (cur_time - task['lastreset']):
        print("This task needs to be reset!")
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
    if args.reset:
        if task['id'] == args.reset:
            print("Resetting task " + str(args.reset))
            task['lastreset'] = cur_time
            task_reset = True

if args.reset and not task_reset:
    print("(!!!) Could not find task " + str(args.reset) + " to reset!")

print("Dumping tasks:")
pprint(tasks)

# Dump stuff back in the file
with open('tasks.json', 'w') as tasks_file:
    dump(tasks, tasks_file)

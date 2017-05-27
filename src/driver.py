#!/usr/bin/env python3

import sched
import time
import json
from pprint import pprint

s = sched.scheduler(time.time, time.sleep)


class TaskEntry(object):
    """
    An entry for a task to be tracked
    """

    def __init__(self, title, resetduration):
        self.title = title
        self.resetduration = resetduration


def jsonDefault(object):
    """
    Translate an object into a dict in order to write to json
    """
    return object.__dict__


def repeat_print(to_print, interval):
    print(to_print)
    s.enter(interval, 1, repeat_print, argument=(to_print, interval))
    s.run()


# Read the stuff from a file.
with open('tasks.json') as tasks_file:
    tasks = json.load(tasks_file)
    pprint(tasks)

title = tasks[0]["title"]
delay = float(tasks[0]["resetduration"])

# Dump stuff in a file for testing.
with open('tasks.json', 'w') as tasks_file:
    json.dump(tasks, tasks_file, default=jsonDefault, indent=2)

# Repeat forever at interval.
repeat_print(title, delay)


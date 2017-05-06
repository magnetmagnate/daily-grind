#!/usr/bin/env python3

import sched
import time
import json

s = sched.scheduler(time.time, time.sleep)

# Scheduler test nonsense


class TaskEntry(object):
    """
    An entry for a task to be tracked
    """

    def __init__(self, title, resetduration):
        self.title = title
        self.resetduration = resetduration


def jsonDefault(object):
    return object.__dict__


def repeat_print(to_print, interval):
    print(to_print)
    s.enter(interval, 1, repeat_print, argument=(to_print, interval))
    s.run()


title = input("Enter some stuff: ")
delay = float(input("Input repeat interval in seconds: "))

entries = [TaskEntry("test1", 5.0)]
entries.append(TaskEntry(title, delay))

# Dump stuff in a file for testing.
with open('data.json', 'w') as data_file:
    json.dump(entries, data_file, default=jsonDefault, indent=2)

# Repeat forever at interval.
repeat_print(title, delay)

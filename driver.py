#!/usr/bin/env python3

import sched, time

s = sched.scheduler(time.time, time.sleep)

# Scheduler test nonsense

def repeat_print(to_print, interval):
    print(to_print)
    s.enter(interval, 1, repeat_print, argument=(to_print, interval))
    s.run()
    

entry = input("Enter some stuff: ")
delay = float(input("Input repeat interval in seconds: "))

# Dump stuff in a file for testing.
with open('data.txt', 'w') as data_file:
    print(entry, file=data_file)

# Repeat forever at interval.
repeat_print(entry, delay)


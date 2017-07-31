#!/usr/bin/env python3

"""
test driver for messing with stuff
"""
from datetime import datetime
from functools import singledispatch
import json
import tz

import pprint
from json_tricks.nonp import dump, load


print('local tz')
print('current time: {0}'.format(datetime.now(tz.LOCAL)))
print('utc offset: {0}'.format(tz.LOCAL.utcoffset(datetime.now(tz.LOCAL))))
print('daylight savings time offset: {0}'.format(
    tz.LOCAL.dst(datetime.now(tz.LOCAL))))
print('TZ name: {0}'.format(tz.LOCAL.tzname(datetime.now(tz.LOCAL))))
print('pacific tz: {0}'.format(tz.PACIFIC))
print('current time: {0}'.format(datetime.now(tz.PACIFIC)))
print('utc offset: {0}'.format(tz.PACIFIC.utcoffset(datetime.now(tz.PACIFIC))))
print('daylight savings time offset: {0}'.format(
    tz.PACIFIC.dst(datetime.now(tz.PACIFIC))))
print('TZ name: {0}'.format(tz.PACIFIC.tzname(datetime.now(tz.PACIFIC))))

# WHEN = datetime.strptime(
#    input(
#        'enter a datetime(format: YYYY-MM-DD HH:mm-0800): '),
#    "%Y-%m-%d %H:%M%z")
# print('{0}'.format(WHEN))

# Test datettime serialization
# https://hynek.me/articles/serialization/ method


@singledispatch
def to_serializable(val):
    """Default call."""
    print("Default call.")
    return str(val)


@to_serializable.register(datetime)
def ts_datetime(val):
    """datetime overload"""
    print("datetime overload call.")
    return val.isoformat() + "Z"

# print(json.dumps(
#    {"Blah": datetime.now()},
#    default=to_serializable
#    ))

with open('testdata.json') as input_file:
    mythingies = load(input_file)

print("\nData from last run:")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(mythingies)

#print(dumps(
#    {"current_time": datetime.now()}
#))

with open('testdata.json', 'w') as output_file:
    dump({"current_time": datetime.now()}, output_file)


"""
test driver for messing with stuff
"""
from datetime import datetime
from tz import LocalTimezone, USTimeZone

LOCAL = LocalTimezone()
EASTERN = USTimeZone(-5, "Eastern", "EST", "EDT")
CENTRAL = USTimeZone(-6, "Central", "CST", "CDT")
MOUNTAIN = USTimeZone(-7, "Mountain", "MST", "MDT")
PACIFIC = USTimeZone(-8, "Pacific", "PST", "PDT")

print('local tz')
print('current time: {0}'.format(datetime.now(LOCAL)))
print('utc offset: {0}'.format(LOCAL.utcoffset(datetime.now(LOCAL))))
print('daylight savings time offset: {0}'.format(LOCAL.dst(datetime.now(LOCAL))))
print('TZ name: {0}'.format(LOCAL.tzname(datetime.now(LOCAL))))
print('pacific tz: {0}'.format(PACIFIC))
print('current time: {0}'.format(datetime.now(PACIFIC)))
print('utc offset: {0}'.format(PACIFIC.utcoffset(datetime.now(PACIFIC))))
print('daylight savings time offset: {0}'.format(PACIFIC.dst(datetime.now(PACIFIC))))
print('TZ name: {0}'.format(PACIFIC.tzname(datetime.now(PACIFIC))))

WHEN = datetime.strptime(
    input(
        'enter a datetime(format: YYYY-MM-DD HH:mm-0800): '),
    "%Y-%m-%d %H:%M%z")
print('{0}'.format(WHEN))


<<<<<<< HEAD
print("test")

=======
"""
test driver for messing with stuff
"""
from datetime import datetime
import tz


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

WHEN = datetime.strptime(
    input(
        'enter a datetime(format: YYYY-MM-DD HH:mm-0800): '),
    "%Y-%m-%d %H:%M%z")
print('{0}'.format(WHEN))
>>>>>>> origin/master

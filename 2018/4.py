import re
import pprint
from datetime import datetime
from collections import defaultdict

"""
[1518-04-06 00:04] Guard #1223 begins shift
[1518-06-10 00:03] falls asleep
[1518-05-25 00:55] wakes up
"""

with open('4.in') as f:
    lines = f.readlines()

datepat = re.compile(r'\[(.*?)\]')


logs = []
for line in lines:
    datepart = datepat.search(line).group(1)
    date = datetime.strptime(datepart,"%Y-%m-%d %H:%M")
    parts = line.split()
    if parts[-1] == 'asleep':
        action = 'S'
    elif parts[-1] == 'up':
        action = 'W'
    else:
        action = int(parts[-3][1:])

    logs.append((date,action))

logs.sort()

guards_sleep = {}

cur_guard = None
sleep_start_minute = None
for log in logs:
    date,action = log
    if type(action) == int:
        cur_guard = action
    elif action == 'W':
        if cur_guard not in guards_sleep:
            guards_sleep[cur_guard] = [0] * 60
        for m in range(sleep_start_minute,date.minute):
            guards_sleep[cur_guard][m] += 1
    else:
        sleep_start_minute = date.minute


# Part I

maxminute = None
maxminutes = 0
maxid = None


for guard in guards_sleep:
    minutes = sum(guards_sleep[guard])
    if minutes > maxminutes:
        maxminutes = minutes
        maxminute = guards_sleep[guard].index(max(guards_sleep[guard]))
        maxid = guard

print(maxid * maxminute)

# Part II

maxminute = None
maxminutefreq = 0
maxid = None


for guard in guards_sleep:
    minutefreq = max(guards_sleep[guard])
    if minutefreq > maxminutefreq:
        maxminutefreq = minutefreq
        maxminute = guards_sleep[guard].index(minutefreq)
        maxid = guard

print(maxid * maxminute)
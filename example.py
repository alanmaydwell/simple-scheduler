#!/usr/bin/env python3

"""
Example of using sched
"""

import time
import datetime
import sched

def ping():
    [x*x*x for x in range(10000000)]
    print(time.strftime("Ping - %H:%M:%S"))

def pong():
    [x*x for x in range(10000000)]
    print(time.strftime("Pong - %H:%M:%S"))

# Define schedule parameters 

# Delay between executions
interval = datetime.timedelta(seconds=5)
# Permitted hours
start_hour, end_hour = 7, 19
# Permitted days of week on which to run (1 = Monday)
days = (1, 2, 3, 4, 5, 6)
# functions/methods to be called
activities = (ping, pong) 

# Start scheduler
sched.schedule_runner(interval, activities, start_hour, end_hour, days)

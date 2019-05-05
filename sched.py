""""
Simple scheduler
Repeatedly calls group of functions/methods at a given interval with option
to restrict running to:
    (a) include only certain days,
    (b) between chosen start hour and end hour
    
Likely has a slight drift as time spent on a few steps in the delay calculation
aren't themselves included in the calculation, but only take teeny fraction of second.

Uses just datetime and time modules. Alternative option would be to use
sched module (or something else) but this seems good enough.
"""

import datetime
import time


def schedule_runner(interval, activities, start_hour=0, end_hour=25,
                    days=(1, 2, 3, 4, 5, 6, 7)):
    """
    Simple scheduler
    Repeatedly calls group of functions/methods at a given interval with option
    to restrict running to:
        (a) include only certain days,
        (b) between chosen start hour and end hour
        
    Likely has a slight drift as time spent on a few steps in the delay calculation
    aren't themselves included in the calculation, but only take teeny fraction of second.

    Uses just datetime and time modules. Alternative option would be to use
    sched module (or something else) but this seems good enough.

    Args:
        interval (datetime.timedelta) - delay between execution of activities
        activities - container (list, tuple) of the functions or methods to be
            periodically executed
        start_hour (int) - optional start hour of day
        end_hour (int) - optional end hour of day
        days - optional days of week on which to run. tuple/list of ints with
               1 representing Monday
    """
    while True:
        activity_start_time = datetime.datetime.now()

        # Execute the scheduled activities if current time within permitted hours and days
        if (start_hour <= activity_start_time.hour <= end_hour and
            activity_start_time.isoweekday() in days):
            for activity in activities:
                activity()

        activity_end_time = datetime.datetime.now()
        execution_time = activity_end_time - activity_start_time

        # Calculate the delay time
        delay = interval - execution_time
        # If we have a positive delay time, wait its duration
        if delay.days >= 0:
            time.sleep(delay.total_seconds())
    


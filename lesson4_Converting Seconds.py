# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#
def convert_seconds(second):
    hour = int(second)/(60*60)
    reminderSecond = second - hour* (60*60)
    minute = int(reminderSecond)/60
    reminderSecond = reminderSecond - minute * 60
    if hour == 1:
        hourstr = 'hour'
    else:
        hourstr = 'hours'
    if minute == 1:
        minstr = 'minute'
    else:
        minstr = 'minutes'
    if reminderSecond ==1:
        secstr = 'second'
    else:
        secstr = 'seconds'
    if type(second)== float:
        return "%d %s, %d %s, %.1f %s" %(hour,hourstr,minute,minstr,reminderSecond,secstr)
    return "%d %s, %d %s, %d %s" %(hour,hourstr,minute,minstr,reminderSecond,secstr)
    

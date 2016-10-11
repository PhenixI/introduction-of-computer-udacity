# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
def convert(second):
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
        return "%d %s, %d %s, %.10f %s" %(hour,hourstr,minute,minstr,reminderSecond,secstr)
    return "%d %s, %d %s, %d %s" %(hour,hourstr,minute,minstr,reminderSecond,secstr)

def convertTobasic(size,units):
    if units == 'kB':
        filesize = size * (2**10) * 8
    elif units == 'MB':
        filesize = size * (2**20) * 8
    elif units == 'GB':
        filesize = size * (2**30) * 8
    elif units == 'TB':
        filesize = size * (2**40)*8
    elif units == 'kb':
        filesize = size * (2**10)
    elif units == 'Mb':
        filesize = size * (2**20)
    elif units == 'Gb':
        filesize = size * (2**30)
    elif units == 'Tb':
        filesize = size * (2**40)
    else:
        return None
        
    return filesize
def download_time(fsize,funit,bandwidth,bandunits):
    filesize = convertTobasic(fsize,funit)
    bwidth = convertTobasic(bandwidth,bandunits)
    
    seconds = filesize/bwidth
    if(seconds * bwidth != filesize):
        seconds = float(filesize)/bwidth
    
    return convert(seconds)

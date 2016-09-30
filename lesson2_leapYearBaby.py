def isLeapYear(year):
    if(year%4 != 0):
        return False
    elif (year%100 != 0):
        return True
    elif (year%400 !=0):
        return False
    else:
        return True

def is_leap_baby(day,month,year):
    return isLeapYear(year) and day == 29 and month ==2

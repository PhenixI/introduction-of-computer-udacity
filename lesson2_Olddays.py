def isLeapYear(year):
    if(year%4 != 0):
        return False
    elif (year%100 != 0):
        return True
    elif (year%400 !=0):
        return False
    else:
        return True

monthDaysLeap= [31,29,31,30,31,30,31,31,30,31,30,31]
monthDaysNotLeap = [31,28,31,30,31,30,31,31,30,31,30,31]

def calDays(year,month,day):
    days = 0        
    if(isLeapYear(year)):
        monthDays = monthDaysLeap
    else:
        monthDays = monthDaysNotLeap
    for i in range(month-1):
        days += monthDays[i]

    days += day
    return days

def calLeftDays(year,month,day):
    if(isLeapYear(year)):
        yearDays = 366
    else:
        yearDays = 365

    days = calDays(year,month,day)
    return yearDays-days

    
def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    i= year1
    days = 0;
    while i<year2:
        if(isLeapYear(i)):
            days += 366
        else:
            days += 365

        i += 1

    year1Days = calDays(year1,month1,day1)
    year2Days = calDays(year2,month2,day2)

    return days + year2Days - year1Days
    

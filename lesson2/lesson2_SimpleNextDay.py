def nextDay(year, month, day):
    if(day == 30):
        day = 1
        if(month==12):
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1
    return year,month,day

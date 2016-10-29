def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    return year2*365+month2*30+day2 - year1*365-month1*30 - day1

def print_line(num):
    str = '|'
    number = 10 -num
    for i in range(number):
        if(i<=4):
            str += '0'
        else:
            str += '*'
    str += '   '
    i = num
    while True:
        if(i>5):
            str += '0'
        elif (i>0):
            str += '*'

        i -= 1
        if(i<=0):
            break;
    str += '|'
    print (str)
                

def print_abacus(number):
    div = 1000000000
    for i in range(10):
        num = number//div
        number = number-div*num
        div //=10
        print_line(num)
        
    

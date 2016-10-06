# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    result = []
    tmp = []
    size = len(string)
    pre = int(string[0])
    i = 1
    result.append(pre)
    while i<size:
        aft = int(string[i])
        if pre >= aft:
            tmp.append(aft)
        else:
            if tmp != []:
                result.append(tmp)
            tmp = []
            pre = aft
            result.append(pre)
        i += 1
    if tmp != []:
        result.append(tmp)
    return result

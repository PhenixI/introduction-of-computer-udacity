def list_mean(list):
    size = len(list)
    sum = 0
    if size == 0:
        print 'the size of list is zero'
        return 
    for i in range(size):
        sum += list[i]

    return sum/size

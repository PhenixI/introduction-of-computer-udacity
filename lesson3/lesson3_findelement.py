def find_element(ls,target):
    index = 0
    for s in ls:
        if(s == target):
            return index
        index += 1
    return -1
        

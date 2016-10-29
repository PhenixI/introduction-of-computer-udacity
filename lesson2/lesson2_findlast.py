def find_last(ss,ts):
    index = -1
    preindex = -1
    while True:
        index = ss.find(ts,index+1)
        if index = -1:
            return preindex
        preindex = index

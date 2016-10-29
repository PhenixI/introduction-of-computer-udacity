def measure_udacity(ls):
    numU = 0
    for str in ls:
        if(str[0]=='U'):
            numU += 1
    return numU

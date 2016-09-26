def set_range(n1,n2,n3):
    if n1>n2:
        big = n1
        small = n2
    else:
        big = n2
        small = n1

    if big > n3:
        big = big
    else:
        big = n3

    if small >n3:
        small = n3
    else:
        small = small

    return big - small

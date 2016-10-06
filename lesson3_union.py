def union(l1,l2):
    for value2 in l2:
        if(value2 not in l1):
            l1.append(value2)
    

def total_enrollment(unilists):
    totalstu=0
    totaltution = 0
    for school in unilists:
        totalstu += school[1]
        totaltution += school[1]*school[2]

    return totalstu,totaltution
    

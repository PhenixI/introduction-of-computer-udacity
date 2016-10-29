def stamps(numP):
    num5=num2=num1=0
    while True:
        if(numP>=5):
            num5 = numP//5
            numP = numP%5
            if(numP == 0):
                break

        if(numP>=2):
            num2 = numP//2
            numP = numP%2
            if(numP == 0):
                break

        if(numP>=0):
            num1 = numP;
            break

    return num5,num2,num1

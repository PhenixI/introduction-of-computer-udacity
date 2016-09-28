def fix_machine(debris,product):
    tarlen = len(product)
    falseStr = "Give me something that's not useless next time."
    for i in range(tarlen):
        index = debris.find(product[i])
        if index == -1:
            return falseStr

    return product
        

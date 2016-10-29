def jungle_animal(animal,my_speed):
    if(animal == 'zebra'):
        print ('Try to ride a zebra!')
    elif(animal == 'cheetah'):
        if(my_speed > 115):
            print('Run!')
        else:
            print('Stay calm and wait!')
    else:
        print('Introduce yourself!')

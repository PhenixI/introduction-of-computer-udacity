
speed_of_light = 300000. # km per second
def speed_fraction(time,distance):
    speed = 2*distance/(time/1000.0)
    return speed/speed_of_light
    

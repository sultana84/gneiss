import math

def to_fahrenheit(degrees_celsius):
    output = degrees_celsius * (9 / 5) + 32
    print(output)
    return output 


def to_celsius(degrees_fahrenheit):
    output = (degrees_fahrenheit - 32) * 5 / 9
    return output


print(to_fahrenheit(0))
print(to_fahrenheit(50))
print(to_fahrenheit(100))
print(to_fahrenheit(150))

print(to_celsius(0))
print(to_celsius(32))
print(to_celsius(100))
print(to_celsius(212))




def get_fall_time(height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8

    # replace with logic of above equation
    time_elapsed = sqrt((2 * height) / acceleration_by_gravity)
    print(time_elapsed)
    return(time_elapsed)


print(get_fall_time(2))
print(get_fall_time(4))
print(get_fall_time(6))
print(get_fall_time(8))
 

def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
    time_in_air = get_fall_time

    tower_range = time_in_air * muzzle_velocity

    delta_x = or:  

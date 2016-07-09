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


gravity = 9.8

def get_fall_time(vertical_height):
    """ get the time in seconds for an object to fall from vertical_height meters """
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8

    time_elapsed = math.sqrt((2 * vertical_height) / acceleration_by_gravity)
    # replace with logic of above equation
    return time_elapsed 

def height(height):
    height = (1/2) * 9.8 * time * time

def time(time):
    time = math.sqrt((2 * height) / gravity)
    return time


print(get_fall_time(2))
print(get_fall_time(4))
print(get_fall_time(6))
print(get_fall_time(8))
 

def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    # update this line to calculate time_in_air using get_fall_time() function
    time_in_air = get_fall_time(tower_height) 

    tower_range = time_in_air * muzzle_velocity

    delta_x = tower_x - target_x  # difference between tower_x and target_y 
    delta_y = tower_y - target_y  # diferrence between tower_y and target_y

    separation = math.sqrt(delta_x**2 + delta_y**2)  # the x and y deltas from a triangle, find the hypotenuse
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?") 
        return True 

    else:
        print("The target is further than the tower range, what should we return?")
        return False 
 

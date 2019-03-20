import numpy as np

# For sake of programming:
output = np.zeros((4, 4))
print(output)
print('______________________')


# Generate the output on LED Grid:
def generate_output(x: int, y: int):
    quadrant = check_quadrant(x, y)

    print('Quadrant : {0}'.format(quadrant))
    x_origin, y_origin = set_edges(quadrant)

    x = abs(x)
    y = abs(y)
    x_index = -1
    y_index = -1

    for i in range(0, 600, 150):
        if x < i:
            break
        else:
            x_index = x_index + 1

    for i in range(0, 600, 150):
        if y < i:
            break
        else:
            y_index = y_index + 1

    print('LED Index : {0}, {1}'.format(x_index, y_index))
    print('______________________')
    x_led, y_led = set_blinker(x_index, y_index, quadrant)
    print(output)
    print('______________________')
    print('1 = Blinking LEDs denoting the Origin.')
    print('8 = Actual bright LED.')
    ouput_to_grid(x_origin, y_origin, x_led, y_led)


# Dedicated to check the quadrant in which the point lies:
def check_quadrant(x: int, y: int) -> int:
    if x > 0 and y > 0:
        return 1

    elif x < 0 < y:
        return 2

    elif x < 0 and y < 0:
        return 3

    elif y < 0 < x:
        return 4

# Setting the Origin of the LED Grid:
def set_edges(q: int):
    if q == 1:
        output[3, 0] = 1
        return 3, 0

    elif q == 2:
        output[3, 3] = 1
        return 3, 3
    
    elif q == 3:
        output[0, 3] = 1
        return 0, 3
        
    elif q == 4:
        output[0, 0] = 1
        return 0, 0

    
# Defining the exact position of LED:
def set_blinker(x: int, y: int, q: int):
    if q == 1:
        output[3-y, x] = 8
        return 3-y, x
    
    elif q == 2:
        output[3-y, 3-x] = 8
        return 3-y, 3-x

    elif q == 3:
        output[y, 3-x] = 8
        return y, 3-x

    elif q == 4:
        output[y, x] = 8
        return y, x
    
        
def output_to_grid(x_origin, y_origin, x_led, y_led):
    
    
    
# Manipulate the values here:
generate_output(100, 100)


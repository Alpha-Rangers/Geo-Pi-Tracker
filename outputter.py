import RPi.GPIO as GPIO
import time
import numpy as np

# Setting up GPIO:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Variable to determine existence of init sequence:
should_run = True

# Configuring output pins:
GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

# For sake of programming:
output = np.zeros((4, 4))
print(output)
print('______________________')

# Mapping the outputs for each LED:
led_map = {
    (0, 0): [True, True, False, True],  # 13
    (0, 1): [True, True, False, False],  # 12
    (0, 2): [True, False, False, True],  # 9
    (0, 3): [True, False, False, False],  # 8
    (1, 0): [True, True, True, True],  # 15
    (1, 1): [True, True, True, False],  # 14
    (1, 2): [True, False, True, True],  # 11
    (1, 3): [True, False, True, False],  # 10
    (2, 0): [False, True, False, True],  # 5
    (2, 1): [False, True, False, False],  # 4
    (2, 2): [False, False, False, True],  # 1
    (2, 3): [False, False, False, False],  # 0
    (3, 0): [False, True, True, True],  # 7
    (3, 1): [False, True, True, False],  # 6
    (3, 2): [False, False, True, True],  # 3
    (3, 3): [False, False, True, False]  # 2
}


def kill_should_run():
    global should_run
    should_run = False

# Init LED sequence:
def call_init_sequence():
    while should_run:
        init_sequence(0, 0)
        init_sequence(0, 3)
        init_sequence(3, 3)
        init_sequence(3, 0)


def init_sequence(x_led, y_led):
    led_values = led_map[(x_led, y_led)]
    GPIO.output(4, led_values[0])
    GPIO.output(18, led_values[1])
    GPIO.output(22, led_values[2])
    GPIO.output(25, led_values[3])

    time.sleep(0.5)


# Generate the output on LED Grid:
def generate_output(x: int, y: int):
    quadrant = check_quadrant(x, y)

    print('Quadrant : {0}'.format(quadrant))
    x_origin, y_origin = set_edges(quadrant)

    x = abs(x)
    y = abs(y)
    x_index = -1
    y_index = -1

    for i in range(0, 10000, 2500):
        if x < i:
            break
        else:
            x_index = x_index + 1

    for i in range(0, 10000, 2500):
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

    output_to_grid(x_origin, y_origin, x_led, y_led)


# Dedicated to check the quadrant in which the point lies:
def check_quadrant(x: int, y: int) -> int:
    if x >= 0 and y >= 0:
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
        output[3 - y, x] = 8
        return 3 - y, x

    elif q == 2:
        output[3 - y, 3 - x] = 8
        return 3 - y, 3 - x

    elif q == 3:
        output[y, 3 - x] = 8
        return y, 3 - x

    elif q == 4:
        output[y, x] = 8
        return y, x


# Final function for output:
def output_to_grid(x_origin, y_origin, x_led, y_led):
    led_values = led_map[(x_led, y_led)]
    origin_values = led_map[(x_origin, y_origin)]

    while True:
        GPIO.output(4, led_values[0])
        GPIO.output(18, led_values[1])
        GPIO.output(22, led_values[2])
        GPIO.output(25, led_values[3])

        time.sleep(0.5)

        GPIO.output(4, origin_values[0])
        GPIO.output(18, origin_values[1])
        GPIO.output(22, origin_values[2])
        GPIO.output(25, origin_values[3])

        time.sleep(0.5)

# Manipulate the values here:
# generate_output(-6000,-6000)

# To play:
# while True:
#    for r in [10, 2600, 5100, 7600]:
#        for c in [10, 2600, 5100, 7600]:
#            generate_output(r,c)
#            time.sleep(0.01)


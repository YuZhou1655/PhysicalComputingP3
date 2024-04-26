import time
import board
import digitalio
import neopixel
import analogio
import pwmio

from adafruit_motor import servo

pwm1 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo1 = servo.Servo(pwm1)
my_servo2 = servo.Servo(pwm2)

# BUTTON_A is an reference to the 2 buttons on the Circuit Python Express
analogin = analogio.AnalogIn(board.A7)

# pull controls the electrical behavoir of the pin
# The standard Pull.DOWN as electricity flows through the pin, switch.value = False(LOW), When the button is pressed, switch.value = True(HIGH)
# Pull.UP inverses the behavior and enables the built in resistor

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.9, auto_write=False)

while True:
    # str() converts variable output into string
    # When adding string + string you get a sentence
    # string + number, string + bool, string + variable wont work
    potVoltage = analogin.value
    potVoltage = (analogin.value * 3.3) /65536
    time.sleep(0.1)
    print("Analog Voltage:" + str(potVoltage))

    if potVoltage >= 0.4:
        my_servo1.angle = 120
        my_servo2.angle = 180
        pixels.fill((255,255,255))
        pixels.show()
    if potVoltage <= 0.399:
        my_servo1.angle = 30
        my_servo2.angle = 80
        pixels.fill((0,0,0))
        pixels.show()
        print("Analog Voltage:" + str(potVoltage))

    pixels.show()

    time.sleep(0.1)  # debounce delay

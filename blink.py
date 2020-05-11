#
# This program is to setup a GPIO output pin to toggle 10 times between high and low values
#
# For Jetson Nano, one can install GPIO module from the following link:
# https://github.com/NVIDIA/jetson-gpio
# and this is compatible with RPi.GPIO
# For Raspberry Pi, RPi.GPIO and gpiozero seem to be installed by default.
#
# Ping He 2020-05-08
#

# Both Raspberry Pi 4 and Jetson Nano can be supported: Mode BCM Pin 18; BOARD Pin 12.
#
import sys
import time

# Check if GPIO module is available or not
try:
    import RPi.GPIO as GPIO
except ImportError:
    print ("Cannot locate RPi.GPIO module!")
    sys.exit(1)

def main():
    
    # Setup BCM Mode
    GPIO.setmode(GPIO.BCM)
    
    # Setup pin number
    pin =  18

    # Setup the pin as output direction
    GPIO.setup(pin, GPIO.OUT)
  
    # Loop 10 times with one second intervals
    for i in range(10):
        # Output pin value high and then sleep for 1 second    
        value = GPIO.HIGH
        GPIO.output(pin, value)
        time.sleep(1)
        
        # Output pin value low and then sleep for 1 second
        value = GPIO.LOW
        GPIO.output(pin, value)
        time.sleep(1)       

    # Clean it up
    GPIO.cleanup()

if __name__ == '__main__':
    main()

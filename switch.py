#
# This program is to turn a GPIO output pin on and off for Raspberry Pi or Jetson Nano
#
# For Jetson Nano, one can install GPIO module from the following link:
# https://github.com/NVIDIA/jetson-gpio
# and this is compatible with RPi.GPIO
# For Raspberry Pi, RPi.GPIO seems to be installed by default.
#
# Ping He 2020-05-012
#

# Both Raspberry Pi 4 and Jetson Nano can be supported
# Please note the mapping between mode and board pins
# For instance: Mode BCM Pin 18 is BOARD Pin 12.
#
# Usage:
# python switch.py (BCM pin number) (1 or 0 -- means on or off)
#
# For instance: 
# python switch.py 18  1
#

import sys

try:
    import RPi.GPIO as GPIO
except ImportError:
    print ("Cannot locate RPi.GPIO module!")
    sys.exit(1)

# Check to see if we have found the system we support
def checkSystem(line):
    if ( ('NVIDIA Jetson Nano' not in line) and ('Raspberry Pi 4' not in line) ): 
        print ("The system is not supported by this program!")
        sys.exit(1)

def main():
    # Exam the system model file
    try:
        with open('/proc/device-tree/model') as f:
            for line in f:
                checkSystem(line)
                break
    except Exception as error:
        print ("The system is not supported by this program!")
        sys.exit(1)

    # Check commandline inputs
    if ( len(sys.argv) < 3 ):
        print ("Please provide two numbers: (BCM pin number; and 1/0 for on/off output)")
        print ("python switch.py number_1  number_2")
        sys.exit(1)

    # Setup BCM Mode
    GPIO.setmode(GPIO.BCM)
    
    # Setup pin number
    pin = int(sys.argv[1])

    # Get on/off instruction
    onoff = sys.argv[2]

    # Suppress warning message 
    # in case the pin was used before
    GPIO.setwarnings(False)

    # Setup the pin as output direction
    GPIO.setup(pin, GPIO.OUT)

    if ( onoff == "1" ):  
        value = GPIO.HIGH
        
    if ( onoff == "0" ):
        value = GPIO.LOW

    GPIO.output(pin, value)

    # Press a key to exit
    print ("Please press a key to exit the program...")
    ch = sys.stdin.read(1)

    # Clean it up
    # Note that the hehaviour on GPIO.cleanp is different between RPi and Jeston
    # the cleanup is commented out
    GPIO.cleanup(pin)

if __name__ == '__main__':
    main()

#!/bin/bash
# Control output of Jetson Nano GPIO 79 or Raspberry Pi 4 GPIO 18
# They both map to pin 12 on the board
#
# Ping He, 2020-05-07

# Check to see if the computer model file exists or not
FILE=/proc/device-tree/model
if [ ! -f "$FILE" ]; then
    echo "Blink only runs on Raspberry Pi 4 or Jetson Nano"
    echo "Please check your computer model"
    exit 0
fi

# Get the computer model string
# You can add elif to support other computer configurations
# with different GPIO pin layouts
model=$(tr -d '\0' < /proc/device-tree/model)

gpio='gpio'

if [[ $model =~ "NVIDIA Jetson Nano" ]]
then
    # Jetson Nano gpio79 is pin 12 on the board
    pin='79'
	
elif [[ $model =~ "Raspberry Pi 4" ]]
then
    # Raspberry Pi 4 gpio18 is pin 12 on the board
    pin='18'
	
else
    echo "Blink only runs on Raspberry Pi 4 or Jetson Nano"
    echo "Please check your computer model"
	
    exit 0
fi

# Setup the GPIO pin
gpiopin="${gpio}""${pin}"
	
# Set the pin to export
echo "${pin}" > /sys/class/gpio/export

# Set Direction to output
echo out > /sys/class/gpio/${gpiopin}/direction

# loop 10 times
for number in {1..10}
do
    echo 1 > /sys/class/gpio/${gpiopin}/value
    sleep 1s
	
    echo 0 > /sys/class/gpio/${gpiopin}/value
	sleep 1s
	
done

# Clean GPIO Pin
echo "${pin}" > /sys/class/gpio/unexport


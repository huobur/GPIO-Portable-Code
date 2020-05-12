# Working with GPIO on Raspberry Pi and Jetson Nano with multiple languages

There have been plenty articles related on how to work with GPIO on Raspberry Pi or Jetson Nano, this project is trying to focus on how to simplify things and write portable programs for each of them to deal with multiple systems.

# 1. System configurations:
Raspberry Pi 4 Model B Rev 1.2 (with Linux raspberrypi 4.19.97-v7l+)
RPi.GPIO was installed on the system (for Python programming)
gcc (Raspbian 8.3.0-6+rpi1) 8.3.0 (for C programming)

Jetson Nano B01 (with Linux jetsonnano 4.9.140-tegra)
NVIDIA Jetson Nano Developer Kit is installed
The following GPIO package is also installed (for Python programming)
https://github.com/NVIDIA/jetson-gpio
gcc (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0 (for C programming)

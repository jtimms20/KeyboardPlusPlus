#!/bin/bash
{
    xterm -e /home/pi/Desktop/boot_KB++.sh
    sleep 1
}& {   #load GUI simultaneously
python3 /home/pi/Desktop/KBpp/main.py
}
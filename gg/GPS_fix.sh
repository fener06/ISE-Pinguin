#!/bin/bash
# Script to start our application
echo "Doing autorun script..."
sudo killall gpsd &
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock &
sudo service ntp restart &
yes "" | command

# Circuit Playground Slouch Detector v1
#
# Compute current angle using accelerometer and compare
# to preset slouch angle. Sound alarm if slouching.
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import math
from adafruit_circuitplayground.express import cpx

SLOUCH_ANGLE    = 10.0
SLOUCH_TIME     = 3
GRAVITY         = 9.80665

# Loop forever
while True:
    # Compute current angle
    current_angle = math.asin(-cpx.acceleration[2] / GRAVITY)
    current_angle = math.degrees(current_angle)
    
    # Check if slouching
    if current_angle > SLOUCH_ANGLE:
        cpx.play_tone(800, 0.5)
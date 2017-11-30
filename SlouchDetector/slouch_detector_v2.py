# Circuit Playground Slouch Detector v2
#
# Push button(s) to set a target angle.
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

# Initialize target angle to zero.
target_angle = 0

# Loop forever
while True:
    # Compute current angle
    current_angle = math.asin(-cpx.acceleration[2] / GRAVITY)
    current_angle = math.degrees(current_angle)
    
    # Set target angle on button press
    if cpx.button_a or cpx.button_b:
        target_angle = current_angle
        cpx.play_tone(900,0.1)
        time.sleep(0.1)
        cpx.play_tone(900,0.1)
        time.sleep(0.1)
        
    # Check if slouching
    if current_angle - target_angle > SLOUCH_ANGLE:
        cpx.play_tone(800, 0.5)
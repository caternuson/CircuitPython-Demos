# Circuit Playground Express Slouch Detector
#
# Push button(s) to set a target angle.
# Compute current angle using accelerometer and compare
# to preset slouch angle. Sound alarm if slouching after
# a preset period of time.
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import math
from adafruit_circuitplayground.express import cpx

SLOUCH_ANGLE    = 10.0
SLOUCH_TIME     = 3
GRAVITY         = 9.80665

# Initialize target angle to zero
target_angle = 0
slouching = False

# Loop forever
while True:
    # Compute current angle
    current_angle = math.asin(-cpx.acceleration[2] / GRAVITY)
    current_angle = math.degrees(current_angle)
    
    # Set target angle on button press
    if cpx.button_a or cpx.button_b:
        target_angle = current_angle
        cpx.play_tone(900, 0.1)
        time.sleep(0.1)
        cpx.play_tone(900, 0.1)
        time.sleep(0.1)
        
    # Check for slouching
    if current_angle - target_angle > SLOUCH_ANGLE:
        if not slouching:
            slouch_start_time = time.monotonic()
        slouching = True
    else:
        slouching = False
        
    # If we are slouching
    if slouching:
        # Check how long we've been slouching
        if time.monotonic() - slouch_start_time > SLOUCH_TIME:
            # Play a tone
            cpx.play_tone(800, 0.5)
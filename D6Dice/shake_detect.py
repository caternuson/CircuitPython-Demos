# Circuit Playground Express Shake Detect
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import math
from adafruit_circuitplayground.express import cpx

# Total acceleration threshold
ROLL_THRESHOLD = 30

# Loop forever
while True:
    # Compute total acceleration
    X = 0
    Y = 0
    Z = 0
    for i in range(10):
        x, y, z = cpx.acceleration
        X = X + x
        Y = Y + y
        Z = Z + z
        time.sleep(0.001)
    X = X / 10
    Y = Y / 10
    Z = Z / 10
    
    total_accel = math.sqrt(X*X + Y*Y + Z*Z)
    
    # Play sound if rolling
    if total_accel > ROLL_THRESHOLD:
        cpx.play_tone(800, 1)
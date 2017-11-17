# Circuit Playground Express Flip Detect
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

while True:
    # Wait for Circuit Playground to be flipped over (face down)
    while cpx.acceleration[2] > 0:
        pass # do nothing
        
    # A little debounce
    time.sleep(0.5)
    
    # Wait for Circuit Playground to be flipped back over (face up)
    while cpx.acceleration[2] < 0:
        pass # do nothing    
    
    # Make a beep noise.
    cpx.play_tone(800, 1)
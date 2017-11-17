# Circuit Playground Express Basic Hourglass
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

while True:
    # Turn ON all the NeoPixels
    cpx.pixels.fill((255, 255, 255))

    # Compute DT
    DT = 5 / 10

    # Turn OFF the NeoPixels one at a time, waiting DT each time
    for p in range(10):
        time.sleep(DT)
        cpx.pixels[p] = (0, 0, 0)  

    # Wait for Circuit Playground to be flipped over (face down)
    while cpx.acceleration[2] > 0:
        pass # do nothing
        
    # A little debounce
    time.sleep(0.5)
    
    # Wait for Circuit Playground to be flipped back over (face up)
    while cpx.acceleration[2] < 0:
        pass # do nothing        
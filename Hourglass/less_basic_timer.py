# Circuit Playground Express Less Basic Timer
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
    
    # Wait for button press to reset timer
    while not cpx.button_a or cpx.button_b:
        pass # do nothing
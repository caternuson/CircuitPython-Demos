# Circuit Playground Express Basic Timer
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

while True:
    # Turn ON all the NeoPixels
    cpx.pixels.fill((255, 255, 255))
    
    # Wait 5 seconds
    time.sleep(5)
    
    # Turn OFF all the NeoPixels
    cpx.pixels.fill((0, 0, 0))    
    
    # Wait for button press to reset timer
    while not cpx.button_a or cpx.button_b:
        pass # do nothing
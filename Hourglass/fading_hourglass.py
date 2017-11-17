# Circuit Playground Express Fading Hourglass
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

COUNT_TIME      = 30  # seconds
FADE_STEPS      = 100 # NeoPixel fade steps
R_SAND          = 255 # Sand color RED value
G_SAND          = 255 # Sand color GREEN value
B_SAND          = 255 # Sand color BLUE value

# Compute per NeoPixel wait time
DT = COUNT_TIME / 10

# Copmute the color value change per fade steps
dr = R_SAND / FADE_STEPS
dg = G_SAND / FADE_STEPS
db = B_SAND / FADE_STEPS

while True:
    # Turn ON all the NeoPixels
    cpx.pixels.fill((R_SAND, G_SAND, B_SAND))
    
    # Loop over each NeoPixel
    for p in range(10):
        # Set the start RGB values
        r = R_SAND
        g = G_SAND
        b = B_SAND
        # Loop over each fading steps
        for n in range(FADE_STEPS):
            time.sleep(DT/FADE_STEPS)
            r = r - dr;
            g = g - dg;
            b = b - db;
            cpx.pixels[p] = (int(r),int(g),int(b))
            
    # Wait for Circuit Playground to be flipped over
    while cpx.acceleration[2] > 0:
        pass
        
    # A little debounce
    time.sleep(0.5)
    
    # Wait for Circuit Playground to be flipped back over
    while cpx.acceleration[2] < 0:
        pass    

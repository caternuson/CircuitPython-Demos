# Circuit Playground Express Bike Light - The All Of Them
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# Change these to set speed (lower is faster)
FLASH_RATE      = 0.250
SPIN_RATE       = 0.100
CYLON_RATE      = 0.100
BEDAZZLE_RATE   = 0.100
CHASE_RATE      = 0.100

# Change these to be whatever color you want
# Use color picker to come up with hex values
FLASH_COLOR     = 0xFF0000
SPIN_COLOR      = 0xFF0000
CYLON_COLOR     = 0xFF0000

# Define 10 colors here.
# Must be 10 entries.
# Use 0x000000 if you want a blank space.
RAINBOW_COLORS = (
  0xFF0000,   
  0xFF5500,
  0xFFFF00,
  0x00FF00,
  0x0000FF,
  0xFF00FF,
  0x000000,
  0x000000,
  0x000000,
  0x000000
)

def buttons_pressed():
    return cpx.button_a or cpx.button_b
    
def flasher():
    while not buttons_pressed():
        # Turn on all the pixels to FLASH_COLOR
        cpx.pixels.fill(FLASH_COLOR)
        
        # Leave them on for a little bit
        time.sleep(FLASH_RATE)
        
        # Turn off all the NeoPixels
        cpx.pixels.fill(0)
        
        # Leave them off for a little bit
        time.sleep(FLASH_RATE)
  
def spinner():
    # Can be any two pixels
    pixel1 = 0
    pixel2 = 5
    
    while not buttons_pressed():
        # Turn off all the NeoPixels
        cpx.pixels.fill(0)
        
        # Turn on two pixels to SPIN_COLOR
        cpx.pixels[pixel1] = SPIN_COLOR
        cpx.pixels[pixel2] = SPIN_COLOR
  
        # Increment pixels to move them around the board
        pixel1 = pixel1 + 1
        pixel2 = pixel2 + 1
        
        # Check pixel values
        pixel1 = pixel1 if pixel1 < 10 else 0
        pixel2 = pixel2 if pixel2 < 10 else 0

        # Wait a little bit so we don't spin too fast
        time.sleep(SPIN_RATE)
    
def cylon():
    pixel1 = 0
    pixel2 = 9

    while not buttons_pressed():
        # Scan in one direction
        for step in range(4):
            cpx.pixels.fill(0)
            
            cpx.pixels[pixel1] = CYLON_COLOR
            cpx.pixels[pixel2] = CYLON_COLOR
            
            pixel1 = pixel1 + 1
            pixel2 = pixel2 - 1
            
            time.sleep(CYLON_RATE)
        
        # Scan back the other direction    
        for step in range(4):
            cpx.pixels.fill(0)
            
            cpx.pixels[pixel1] = CYLON_COLOR
            cpx.pixels[pixel2] = CYLON_COLOR
            
            pixel1 = pixel1 - 1
            pixel2 = pixel2 + 1
            
            time.sleep(CYLON_RATE)

def bedazzler():
    while not buttons_pressed():
        # Turn off all the NeoPixels
        cpx.pixels.fill(0)
        
        # Turn on a random pixel to a random color
        cpx.pixels[random.randrange(10)] = ( random.randrange(256),
                                             random.randrange(256),
                                             random.randrange(256) )
    
        # Leave it on for a little bit
        time.sleep(BEDAZZLE_RATE)

def rainbow():
    # Start at the beginning
    start_color = 0

    while not buttons_pressed():
        # Turn off all the NeoPixels
        cpx.pixels.fill(0)

        # Loop through and set pixels
        color = start_color
        for p in range(10):
            cpx.pixels[p] = RAINBOW_COLORS[color]
            color += 1
            color = color if color < 10 else 0
            
        # Increment start index into color array
        start_color += 1
        
        # Check value and reset if necessary
        start_color = start_color if start_color < 10 else 0
        
        # Wait a little bit so we don't spin too fast
        time.sleep(CHASE_RATE)
        
# Loop forever
while True:
    flasher()   ; time.sleep(0.25)
    spinner()   ; time.sleep(0.25)
    cylon()     ; time.sleep(0.25)
    bedazzler() ; time.sleep(0.25)
    rainbow()   ; time.sleep(0.25)
    #
    # TODO: add your animation here!
    #
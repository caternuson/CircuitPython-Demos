# Circuit Playground Express Random Demo
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# Loop forever
while True:
    # Wait for button press
    while not cpx.button_a and not cpx.button_b:
        # Do nothing
        pass
    
    # Print a random number
    print(random.randrange(1,7))
    
    # Debounce delay
    time.sleep(0.5)
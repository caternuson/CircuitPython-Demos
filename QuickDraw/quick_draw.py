# Circuit Playground Express Quick Draw
# 
# Who's faster?
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from analogio import AnalogIn
import board
from adafruit_circuitplayground.express import cpx

SHORTEST_DELAY = 1  # seconds
LONGEST_DELAY  = 10 #    "
PLAYER_PIXELS = {
  1 : (0,1,2,3,4),
  2 : (5,6,7,8,9)
}

def show_outcome(player, winner):
    # Turn them all off
    cpx.pixels.fill(0)
    
    # Set pixel color
    if winner:
        color = 0x00FF00
    else:
        color = 0xFF0000

    # Show which player won/lost
    for p in PLAYER_PIXELS[player]:
        cpx.pixels[p] = color
    
    # Play a little tune
    if winner:
        cpx.play_tone(800, 0.2)
        cpx.play_tone(900, 0.2)
        cpx.play_tone(1400, 0.2)
        cpx.play_tone(1100, 0.2)
    else:
        cpx.play_tone(200, 1)

    # Sit here forever
    while True:
        pass      

# Seed the random function with noise
a4 = AnalogIn(board.A4)
a5 = AnalogIn(board.A5)
a6 = AnalogIn(board.A6)
a7 = AnalogIn(board.A7)

seed  = a4.value
seed += a5.value
seed += a6.value
seed += a7.value

random.seed(seed)

# Wait a random amount of time
count_time = random.randrange(SHORTEST_DELAY, LONGEST_DELAY+1)
start_time = time.monotonic()
while time.monotonic() - start_time < count_time:
    # Check if player draws too soon
    if cpx.button_a:
        show_outcome(1, False)
    if cpx.button_b:
        show_outcome(2, False)    

# Turn on all the NeoPixels
cpx.pixels.fill(0xFFFFFF)

# Check for player draws
while True:
    if cpx.button_a:
        show_outcome(1, True)
    if cpx.button_b:
        show_outcome(2, True)
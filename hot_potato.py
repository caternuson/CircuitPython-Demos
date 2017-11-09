# Circuit Playground Express Hot Potato
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
import math
import board
from analogio import AnalogIn
from adafruit_circuitplayground.express import cpx

# This brings in the song to play
import melody
number_of_notes = len(melody.melody)

SHAKE_THRESHOLD = 30

def get_total_accel():
    # Compute total acceleration
    X = 0
    Y = 0
    Z = 0
    for count in range(10):
        x,y,z = cpx.acceleration
        X = X + x
        Y = Y + y
        Z = Z + z
        time.sleep(0.001)
    X = X / 10
    Y = Y / 10
    Z = Z / 10

    return math.sqrt(X*X + Y*Y + Z*Z)

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

# Set the NeoPixels all red    
cpx.pixels.fill(0xFF0000)

# Loop forever
while True:
    # Wait for shaking
    while get_total_accel() < SHAKE_THRESHOLD:
        pass  # do nothing
    
    # Game length
    game_length = random.randint(number_of_notes, 6*number_of_notes)
    
    # Game play with melody
    note_to_play = 0
    for game_step in range(game_length):
        
        # Add some flare using the NeoPixels
        cpx.pixels.fill(0)
        cpx.pixels[random.randint(0,9)] = ( random.randint(0,255),
                                            random.randint(0,255),
                                            random.randint(0,255) )
        
        # Play the note
        note_duration = 1 / melody.tempo[note_to_play]
        note = melody.melody[note_to_play]
        note = note if note <= 3500 else 3500
        if note == 0:
            time.sleep(note_duration)
        else:
            cpx.play_tone(melody.melody[note_to_play], note_duration)
        
        # Increment and check the note counter
        note_to_play += 1
        note_to_play = note_to_play if note_to_play < number_of_notes else 0
    
    #    
    # GAME OVER
    #
    
    # Set the NeoPixels all red
    cpx.pixels.fill(0xFF0000)
    
    # Delay a bit so can't just reset with a shake
    time.sleep(2)
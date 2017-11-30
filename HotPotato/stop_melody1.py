# Circuit Playground Express Stop Melody 1
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import random
from adafruit_circuitplayground.express import cpx

# This brings in the song to play
import melody
number_of_notes = len(melody.melody)

# Loop forever
while True:
    if cpx.button_a or cpx.button_b:
        game_length = random.randrange(len(melody.melody))
        for i in range(game_length):
            note_duration = 1 / melody.tempo[i]
            note = melody.melody[i]
            if note == 0:
                time.sleep(note_duration)
            else:
                cpx.play_tone(note, note_duration)
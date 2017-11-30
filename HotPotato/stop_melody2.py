# Circuit Playground Express Stop Melody 2
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
        game_length = random.randint(number_of_notes, 6*number_of_notes)        
        note_to_play = 0
        for i in range(game_length):
            note_duration = 1 / melody.tempo[note_to_play]
            note = melody.melody[note_to_play]
            if note == 0:
                time.sleep(note_duration)
            else:
                cpx.play_tone(note, note_duration)
            note_to_play += 1
            note_to_play = note_to_play if note_to_play < number_of_notes else 0                
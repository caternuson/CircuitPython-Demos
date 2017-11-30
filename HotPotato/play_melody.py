import time
from pitches import *
from adafruit_circuitplayground.express import cpx

# notes in the melody:
melody = (
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
)

# note durations: 4 = quarter note, 8 = eighth note, etc.:
tempo = (
  4, 8, 8, 4, 4, 4, 4, 4
)

# Loop forever
while True:
    if cpx.button_a or cpx.button_b:
        for i in range(len(melody)):
            note_duration = 1 / tempo[i]
            note = melody[i]
            if note == 0:
                time.sleep(note_duration)
            else:
                cpx.play_tone(note, note_duration)
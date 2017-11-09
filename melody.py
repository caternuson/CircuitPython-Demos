# Mario theme code by Dipto Pratyaksa
# http://www.linuxcircle.com/2013/03/31/playing-mario-bros-tune-with-arduino-and-piezo-buzzer/
#
# dropped an octave to work with current CircuitPython CPX library

from pitches import *

melody = (
  NOTE_E6, NOTE_E6, 0, NOTE_E6, 
  0, NOTE_C6, NOTE_E6, 0,
  NOTE_G6, 0, 0,  0,
  NOTE_G5, 0, 0, 0, 

  NOTE_C6, 0, 0, NOTE_G5, 
  0, 0, NOTE_E5, 0, 
  0, NOTE_A5, 0, NOTE_B5, 
  0, NOTE_AS5, NOTE_A5, 0, 

  NOTE_G5, NOTE_E6, NOTE_G6, 
  NOTE_A6, 0, NOTE_F6, NOTE_G6, 
  0, NOTE_E6, 0,NOTE_C6, 
  NOTE_D6, NOTE_B5, 0, 0,

  NOTE_C6, 0, 0, NOTE_G5, 
  0, 0, NOTE_E5, 0, 
  0, NOTE_A5, 0, NOTE_B5, 
  0, NOTE_AS5, NOTE_A5, 0, 

  NOTE_G5, NOTE_E6, NOTE_G6, 
  NOTE_A6, 0, NOTE_F6, NOTE_G6, 
  0, NOTE_E6, 0,NOTE_C6, 
  NOTE_D6, NOTE_B5, 0, 0
)

tempo = (
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
)
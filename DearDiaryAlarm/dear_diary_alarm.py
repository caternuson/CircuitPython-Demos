# Circuit Playground Express Dear Diary Alarm
# 
# Don't let sister/brother read your secrets! Place the "armed" Circuit
# Playground under your diary. If someone tries to remove the diary, an alarm
# will sound.
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

# Set alarm threshold
ALARM_THRESHOLD = 20

# Turn on all the NeoPixels
cpx.pixels.fill((255,0,0))

# Wait for button press
while (cpx.button_a == False) and (cpx.button_b == False):
    # Do nothing
    pass

# Countdown timer
for p in range(10):
    cpx.pixels[p] = 0
    time.sleep(0.5)
    
# Compute covered light sensor value
covered_value = 0
for count in range(5):
    covered_value = covered_value + cpx.light
covered_value = covered_value / 5

# Beep to indicate armed
cpx.play_tone(1000, 1)

# Begin alarm
triggered = False
while True:
    if triggered:
        cpx.play_tone(2000, 0.5)
        time.sleep(0.5)
        cpx.play_tone(3000, 0.5)
        time.sleep(0.5)        
    if cpx.light > covered_value + ALARM_THRESHOLD:
        triggered = True

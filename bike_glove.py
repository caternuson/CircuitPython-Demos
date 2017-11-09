# Circuit Playground Express Bike Glove - With "On/Off"
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
from adafruit_circuitplayground.express import cpx

THRESHOLD_UP        = 5   # threshold for hand up test
THRESHOLD_RIGHT     = 5   # threshold for right turn
THRESHOLD_LEFT      = -5  # threshold for left turn

LEFT_COLOR          = 0xFFFFFF
RIGHT_COLOR         = 0xFFFFFF
ANIM_DELAY          = 0.200

RIGHT_TURN = (
  (2, 5, 6, 7, 8, 9),
)

LEFT_TURN = (
  (5, 4),
  (6, 3),
  (7, 2),
  (8, 1),
  (9, 0)
)

def animate_glove(animation, color, delay=ANIM_DELAY):
    for frame in animation:
        cpx.pixels.fill(0)
        for pixel in frame:
            cpx.pixels[pixel] = color
        time.sleep(delay)
        
    cpx.pixels.fill(0)
    time.sleep(ANIM_DELAY)

# Loop forever
while True:
    # Check slide switch position
    if cpx.switch:
        # Get acceleration values
        X, Y, Z = cpx.acceleration
        # Check if glove is down or up
        if Z < THRESHOLD_UP:
            # Determine glove orienation and animate
            if Y > THRESHOLD_RIGHT:
                animate_glove(RIGHT_TURN, RIGHT_COLOR)
            elif X > THRESHOLD_LEFT:
                animate_glove(LEFT_TURN, LEFT_COLOR)
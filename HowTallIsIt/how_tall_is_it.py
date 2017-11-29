# Circuit Playground Express How Tall Is It
#
# Uses the accelerometer to turn the Circuit Playground into an inclinometer.
# Can be used to determine the height of objects using a little right angle
# math.
#
# Author: Carter Nelson
# MIT License (https://opensource.org/licenses/MIT)
import time
import math
from adafruit_circuitplayground.express import cpx

# Indicate ready using NeoPixel 9.
# Set it red to indicate no good reading yet.
cpx.pixels[9] = ((255, 0, 0))

while True:
    if (cpx.button_a or cpx.button_b):
        # Compute average
        X = 0
        Y = 0
        Z = 0
        for count in range(10):
            x,y,z = cpx.acceleration
            X = X + x
            Y = Y + y
            Z = Z + z
            time.sleep(0.01)
        X = X / 10
        Y = Y / 10
        Z = Z / 10

        # Compute angle
        angle = math.atan2(-X, Y)

        # Compute total acceleration
        total_accel = math.sqrt(X*X + Y*Y + Z*Z)

        # Initially assume the reading is good
        good_reading = True

        # Check for levelness
        # Ideally Z=0, but allow a small amount of Z
        if abs(Z) > 1.0:
            good_reading = False

        # Check for motion
        # Gravity (9.8 m/s^2) should be the only acceleration, but allow a small amount of motion.
        if total_accel > 10:
            good_reading = False

        # Indicate if reading was good
        if good_reading:
            # Green light
            cpx.pixels[9] = (0, 255, 0)
        else:
            # Red light
            cpx.pixels[9] = (255, 0, 0)

        # Indicate sign of angle
        if angle < 0:
            # Blue light
            cpx.pixels[8] = (0, 0, 255)
        else:
            # Off
            cpx.pixels[8] = (0, 0, 0)

        # Display angle magnitude, in degrees, on NeoPixels 0-7 as 8 bit value.
        # 1 = NeoPixel ON, 0 = NeoPixel OFF
        angle_display = int(abs(angle * 57.29578))
        for p in range(8):
            if angle_display &0x01 == 1:
                # Turn on the NeoPixel
                cpx.pixels[p] = (255, 255, 255)
            else :
                # Turn off the NeoPixel
                cpx.pixels[p] = (0, 0, 0)
            angle_display = angle_display >> 1

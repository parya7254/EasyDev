# Test code for driving the integrated NeoPixel LED onboard the EasyDev RP2040 Dev Board!
# Code by Arya Patel (@parya7254 on GitHub)

# This will import all of the libraries needed to run the code
import time
import board
import neopixel
from neopixel_write import neopixel_write
import time
from adafruit_led_animation.animation.rainbow import Rainbow

# This will declare the pin that the LED is connected to (internally) and provide the number of pixels to drive
# If you also want to drive other LEDs using the unboard dedicated RGBA pin, increase the num_pixels to the length of the strip/number of LEDs you want to drive + 1
RGBPin = board.GP25
num_pixels = 1

# This will assign the NeoPixel and animation to objects so that they can easily be used in code
pixels = neopixel.NeoPixel(RGBPin, num_pixels, brightness=1, auto_write = False)
rainbowAnimationSmooth = Rainbow(pixels, speed=0.02, period = 2)

# This will flash the colors of the rainbow through the LED without any transition in between
def colorCycle():
    pixels.fill(255,0,0)
    pixels.show()
    time.sleep(0.4)
    pixels.fill(255,217,0)
    pixels.show()
    time.sleep(0.4)
    pixels.fill(72,255,0)
    pixels.show()
    time.sleep(0.4)
    pixels.fill(0,255,0)
    pixels.show()
    time.sleep(0.4)
    pixels.fill(0,0,255)
    pixels.show()
    time.sleep(0.4)
    pixels.fill(255,0,255)
    pixels.show()
    time.sleep(0.4)

# This will solidly cycle through the colors one time on the LED without and smoothing
colorCycle()

while True:
    # This will fade through the colors of the rainbow on the LED
    rainbowAnimationSmooth.animate()
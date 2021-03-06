#!/bin/python

# Skyler Ogden
# 11/23/2017


# Initial script

# Purpose
# Translate printer status into light indication code


import requests
import json
import time
# from numpy import interp
from neopixel import *

# Octoprint:
# Use api key
# http://docs.octoprint.org/en/master/api/


# Dependant code libraries:

# phue
# Full featured Python library to control the Philips Hue lighting system.
# https://github.com/studioimaginaire/phue

# color converter


# debug flag
# debug = 0 - off
# debug = 1 -

octoprint_api = '56D0FF611C184738B2CAE37CE1F7446F'
octoprint_ip = 'printerpi.lan'
LED_COUNT = 61  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW

# Bed = 61 Lights
# Heat =

bed_target_prev = 0
bed_target_new = 0
temperature_percentage_new = 0
temperature_percentage_old = 0
LED_min_value = 10
LED_max_value = 255
temperature_ambient = 25.0  # Ambient temperature in C


def octoprint_getstatus(object, value, status):
    # Get current print state
    request = requests.get('http://printerpi.lan/api/printer?history=true&limit=2',
                           headers={'X-Api-Key': '56D0FF611C184738B2CAE37CE1F7446F'})
    parsed_request = json.loads(request.content)
    value_read = parsed_request[value][object][status]
    return value_read

def set_led(status):
    # [bed_actual, bed_target]
    # Color(green, red, blue)
    print "\n"
    bed_actual = status[0]
    bed_target = status[1]

    if bed_target == 0:
        # When bed isn't heating up just show colors
        print 'cooldown detected'
        # For the bed, we assume a maximum temperature of 120 degrees
        cooldown_percent = get_percent(temperature_ambient, 240, bed_actual)


        rgb_red = map_range(0, 100, cooldown_percent, 0, 255)
        print 'cooldown_percentage: {}'.format(cooldown_percent)
        print [0, rgb_red, 255 - rgb_red]

        for j in xrange(0, LED_COUNT):
            # Set the rest of the LEDs color
            # Set LEDs to Blue

            strip.setPixelColor(j, Color(255 - rgb_red, rgb_red, 0))
            strip.show()
    else:
        temperature_percent = get_percent(temperature_ambient, bed_target, bed_actual)

        print 'status values: {}, {}'.format(bed_actual, bed_target)
        print 'temperature percentage: {}'.format(temperature_percent)

        LED_current = int(round(LED_COUNT * (float(temperature_percent) / 100.0)))
        print 'led_current: {}'.format(LED_current)


        for j in xrange(0, LED_current):
            # Set LEDs to RED
            strip.setPixelColor(j, Color(0, 255, 0))
            strip.show()

        for j in xrange(LED_current, LED_COUNT):
            # Set the rest of the LEDs color
            # Set LEDs to Green
            strip.setPixelColor(j, Color(255, 0, 0))
            strip.show()

    return

def get_percent(min_value, max_value, actual):
    # actual value may be outside the range [min_value, max_value]
    # returns 0 if actual < min_value and 100 if actual > max_value
    percent = int(round( 100 * ((actual - min_value) / (max_value - min_value))))
    if percent < 0:
        percent = 0

    elif percent > 100:
        percent = 100

    # returns integer
    return percent

def map_range(in_min, in_max, actual, out_min, out_max):
    # maps an input range and actual value to an output range

  return int(round((float(actual) - in_min) * (out_max - out_min) / (in_max - in_min) + out_min))



if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                              LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    while True:

        # Get tool0 temperature
        status = octoprint_getstatus('tool0', 'temperature', 'actual'), \
                 octoprint_getstatus('tool0', 'temperature', 'target')
        set_led(status)
        time.sleep(0.04)


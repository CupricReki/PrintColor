#!/bin/python

# Skyler Ogden
# 11/23/2017


# Initial script

# Purpose
# Translate printer status into light indication code


import requests
import json
import time
# from neopixel import *

#Octoprint:
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
LED_COUNT      = 220      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW


# Initiate variables
bed_start = 0


def octoprint_getstatus():
    # Get current print state
    request = requests.get('http://printerpi.lan/api/printer?history=true&limit=2', headers = {'X-Api-Key': '56D0FF611C184738B2CAE37CE1F7446F'})
    parsed_request = json.loads(request.content)
    bed_actual = parsed_request['temperature']['bed']['actual']
    bed_target = parsed_request['temperature']['bed']['target']
    return[bed_actual, bed_target]
    # Get target and current temperature

def set_led():
    # Code will go here
    print(strip)
    return
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
    # LED_STRIP)
    # Intialize the library (must be called once before other functions).
    #strip.begin()
    while True:
        print(octoprint_getstatus())
        print
        time.sleep(50)
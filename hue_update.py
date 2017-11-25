#!/bin/python

# Skyler Ogden
# 11/23/2017


# Initial script

# Purpose
Translate printer status into light indication code


TODO

Read states from octoprint
Write RGB to hue lights
Sync Hue light to temperature
Sync Hue light to printer status
Sync RGBW neopixel strip to temperature
Sync RGBW neopixel strip to print status by filling up a bar

Octoprint:

http://docs.octoprint.org/en/master/api/


# Dependant code libraries:

# phue
# Full featured Python library to control the Philips Hue lighting system.
https://github.com/studioimaginaire/phue

# color converter



# debug flag
# debug = 0 - off
# debug = 1 -

octoprint_api = 'apikey'
octoprint_ip = '10.10.0.110'


def get_octoprint_temp():
    # Get target and current temperature

    if debug


def get_octoprint_status():
    # Get print status

def update_huelight(color, brightness):
    if brightness != '':
        brightness = 255

    # Takes in the desired color (in RGB) and translates it into the correct x,y colord
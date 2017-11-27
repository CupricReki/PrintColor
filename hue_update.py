#!/bin/python

# Skyler Ogden
# 11/23/2017


# Initial script

# Purpose
# Translate printer status into light indication code


import requests

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


def octoprint():
    r = requests.get('http://printerpi.lan/api/printer?history=true&limit=2', headers = {'X-Api-Key': '56D0FF611C184738B2CAE37CE1F7446F'})
    # Get target and current temperature


octoprint()
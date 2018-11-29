import sys
import time
import Adafruit_DHT
import httplib, urllib
import json
import RPi.GPIO as GPIO
import requests
import socket
import threading
import logging
import mraa
deviceId = "DJHgkzrj"
deviceKey = "bP3HwPHSqVmHmvnO"
logging.basicConfig(level='INFO')
def establishCommandChannel():
        connectionAPI = 'https://api.mediatek.com/mcs/v2/devices/%(device_id)s/$
        r = requests.get(connectionAPI % DEVICE_INFO,
                 headers = {'deviceKey' : DEVICE_INFO['device_key'],
                            'Content-Type' : 'text/csv'})
        logging.info("Command Channel IP,port=" + r.text)
        (ip, port) = r.text.split(',')

    # Connect to command server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.settimeout(None)

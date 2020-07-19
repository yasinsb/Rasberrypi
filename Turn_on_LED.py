# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:40:12 2020

@author: EngenhariaCecal
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)

# sudo python LED.py


#!/usr/bin/python
import sys
import Adafruit_DHT


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)



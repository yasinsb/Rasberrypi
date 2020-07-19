# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:40:12 2020

@author: EngenhariaCecal
"""

import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))

# sudo python Temperature_Humidity.py









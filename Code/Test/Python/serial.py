# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:28:07 2022

@author: techv
"""

import serial
ser = serial.Serial("COM18",9600)


data = "Hi i am Python\n"

ser.write(data.encode())

print(ser.readline())
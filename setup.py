#! /usr/bin/env python
# Akshay Singh
# To put interface on monitor mode, for the use of app1.py

import subprocess

user_input = raw_input("Enter your Interface(wlan1, wlan0 or any other): ")

call_1 = subprocess.call(["airmon-ng","start",user_input])


print("Monitor mode started on: ", user_input)






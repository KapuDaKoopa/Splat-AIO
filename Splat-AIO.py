# Rewritten for a second time. Hopefully cleaner
import os, sys, subprocess, time
from tcpgecko import TCPGecko
#import common

# check to see if setup has already been completed

if os.path.isfile("./Resources/setup/ip.txt") == True:
    ip = open("./Resources/setup/ip.txt", "r").read()
    
    

#Ask for the IP and save it to ip.txt to be read on next launch
else:
    print("""What is your Wii U's IP address? This will be set to every script
so that they run properly, and you can change this later.
Example: 192.168.1.114\n""")
    fresh_ip = raw_input(">> ")
    save = open("./Resources/setup/ip.txt", "w")
    save.write(fresh_ip)
    save.close()
    ip = fresh_ip

execfile("./Resources/setup/update_beta.py")

execfile("./Resources/run/main/menu.py")

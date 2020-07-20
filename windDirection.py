#!/usr/bin/env python3

# Partially inspired by:
#SPoschandler.py written by Robin Newman, July 2017

# Updates by Elias Berkhout, for Allan Giddy
# July 2020

# This program requires gpiod daemon to be running. Install it with:
# sudo apt-get update followed by sudo apt-get install pigpio
# Set it to autostart on boot with:
# sudo systemctl enable pigpiod.service (followed by a reboot)
# The program also requires gpiozero to be installed, and python-osc


# import a few libraries
from gpiozero import Button # button objects from gpiozero library
import random # for testing purposes
from pythonosc import osc_message_builder # build the OSC messages to send to sonic pi
from pythonosc import udp_client # client to setup OSC communication
from time import sleep # to slow the script down a bit, wait for new values, etc

# declare the sender for OSC messages -- localhost IP and sonic pi default port for OSC
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

# create array of switch pins
# switches = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

N = Button(2)
NNE = Button(3)
NE = Button(4)
ENE = Button(5)
E = Button(6)
ESE = Button(7)
SE = Button(8)
SSE = Button(9)
S = Button(10)
SSW = Button(11)
SW = Button(12)
WSW = Button(13)
W = Button(14)
WNW = Button(15)
NW = Button(16)
NNW = Button(17)

# function for sending direction message to sonic pi
# direction value required when calling the function
def msg(dir):
    message = osc_message_builder.OscMessageBuilder(address = '/play')    # create the message, for address /sonicPi/play 
    message.add_arg(dir, arg_type = 'i')                                         # add the direction argument to the message
    message = message.build()                                                   # build the message
    sender.send(message)                                                       # send it
    
if __name__ == "__main__":
    try:
        while( True ):
            # val = random.randrange(91, 106)
            if N.is_pressed: msg(0); print('N')
            elif NNE.is_pressed: msg(1); print('NNE')
            elif NE.is_pressed: msg(2); print('NE')
            elif ENE.is_pressed: msg(3); print('ENE')
            elif E.is_pressed: msg(4); print('E')
            elif ESE.is_pressed: msg(5); print('ESE')
            elif SE.is_pressed: msg(6); print('SE')
            elif SSE.is_pressed: msg(7); print('SSE')
            elif S.is_pressed: msg(8); print('S')
            elif SSW.is_pressed: msg(9); print('SSW')
            elif SW.is_pressed: msg(10); print('SW')
            elif WSW.is_pressed: msg(11); print('WSW')
            elif W.is_pressed: msg(12); print('W')
            elif WNW.is_pressed: msg(13); print('WNW')
            elif NW.is_pressed: msg(14); print('NW')
            elif NNW.is_pressed: msg(15); print('NNW')
            #print(val)
            #msg(val)
            sleep(1)
    except ( KeyboardInterrupt ):
        exit()
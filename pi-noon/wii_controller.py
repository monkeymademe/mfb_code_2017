# Based of the CamJam EduKit 3 - Robotics kit code found https://github.com/recantha/EduKit3-Bluetooth
# Wii controller remote control script using the explorer hat pro

import explorerhat
import time # Import the Time library
import os

eh = explorerhat

# Turn all motors off
def StopMotors():
    eh.motor.one.speed(0)
    eh.motor.two.speed(0)

# Turn both motors forwards
def Forwards():
    eh.motor.one.speed(100)
    eh.motor.two.speed(100)

# Turn both motors backwards
def Backwards():
    eh.motor.one.speed(-100)
    eh.motor.two.speed(-100)

def Left():
    eh.motor.one.speed(-100)
    eh.motor.two.speed(100)

def Right():
    eh.motor.one.speed(100)
    eh.motor.two.speed(-100)

StopMotors()

# Credit for this part must go to:
# Author : Matt Hawkins (adapted by Michael Horne and then updated to use the explorer hat pro by James Mitchell) 
# http://www.raspberrypi-spy.co.uk/?p=1101
# -----------------------
# Import required Python libraries
# -----------------------
import cwiid

eh.light[0].on()
button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
eh.light[0].on()
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
    wii=cwiid.Wiimote()
    eh.light[0].off()
    eh.light[3].on()

except RuntimeError:
    print "Error opening wiimote connection"
    eh.light[2].on()
    eh.light[3].off()
    # Uncomment this line to shutdown the Pi if pairing fails
    #os.system("sudo halt")
    quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']

    # If Plus and Minus buttons pressed
    # together then rumble and quit.
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
        print '\nClosing connection ...'
        wii.rumble = 1
        eh.light[2].on()
        time.sleep(1)
        wii.rumble = 0
        os.system("sudo halt")
        exit(wii)
  
    # Check if other buttons are pressed by
    # doing a bitwise AND of the buttons number
    # and the predefined constant for that button.
    if (buttons & cwiid.BTN_LEFT):
        print 'Left pressed'
        Backwards()
        time.sleep(button_delay)         

    elif(buttons & cwiid.BTN_RIGHT):
        print 'Right pressed'
        Forwards()
        time.sleep(button_delay)          

    elif (buttons & cwiid.BTN_UP):
        print 'Up pressed' 
        Left()       
        time.sleep(button_delay)          
    
    elif (buttons & cwiid.BTN_DOWN):
        print 'Down pressed'      
        Right()
        time.sleep(button_delay)  
    
    else:
        StopMotors()

# CamJam EduKit 3 - Robotics
# Wii controller remote control script

import explorerhat
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
import os

eh = explorerhat

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

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
# Author : Matt Hawkins (adapted by Michael Horne)
# http://www.raspberrypi-spy.co.uk/?p=1101
# -----------------------
# Import required Python libraries
# -----------------------
import cwiid

explorerhat.light[0].on()
button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
explorerhat.light[0].on()
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
    wii=cwiid.Wiimote()
    explorerhat.light[0].off()
    explorerhat.light[3].on()

except RuntimeError:
    print "Error opening wiimote connection"
    explorerhat.light[2].on()
    explorerhat.light[3].off()
    # Uncomment this line to shutdown the Pi if pairing fails
    #os.system("sudo halt")
    quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

#for x in range(0,3):
#    GPIO.output(PIN_LED, 1)
#    time.sleep(0.25)
#    GPIO.output(PIN_LED, 0)
#    time.sleep(0.25)

wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']

    # If Plus and Minus buttons pressed
    # together then rumble and quit.
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
        print '\nClosing connection ...'
        wii.rumble = 1
        explorerhat.light[2].on()
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

# -*- coding: utf-8-*-
import random
import re
from client import jasperpath
import RPi.GPIO as GPIO
import time
import sys
import vibrate

WORDS = ["HELLO"]


def handle(text, mic, profile):
    
    vibrate.retrieve_from_DOA('low')
    print("hello module")
    mic.say('hello')
    
    
        
def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bhello\b', text, re.IGNORECASE))

    
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    
    try:
        global motorLeft
        global motorRight
        
        GPIO.setmode(GPIO.BCM)
        #GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        
        motorLeft = GPIO.PWM(18,100) #motor left = yellow
        motorLeft.start(0)
        motorRight = GPIO.PWM(23,100) #motor right = blue
        motorRight.start(0)
        
        print("motor vibrating")
        mic.say("vibration")
        retrieve_from_DOA()
        
        #direction = retrieve_from_DOA()
        #print("direction: " + direction)
        #if direction == 'left':
            #print("left motor running")
            
            #for x in range(num):
                #motorLeft.ChangeDutyCycle(80)
                #time.sleep(0.5)
                #motorLeft.ChangeDutyCycle(0)
                #time.sleep(0.2)
            
        #if direction == 'right':
            #print("right motor running")
    
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("Keyboard interrupt")

    finally:
        motorLeft.stop()
        motorRight.stop()
        motorLeft = None
        motorRight = None
        GPIO.cleanup() # cleanup all GPIO
        print("clean up")
        
    
    
def retrieve_from_DOA():
    sys.path.append('/home/pi/reverb/usb_4_mic_array')
    import DOA
    doa = DOA.main()
    if (doa < 90 and doa >= 0) or (doa >= 270):
        print("motor DOA <90 or >= 270: " + str(doa))
        #return ("right")
        
        #vibrate_motor("right")
        
        vibrate.start_vibrate('right', 50, 3)
        
    elif (doa >= 90 and doa < 270):
        print ("motor DOA >90: " + str(doa))
        #return("left")
        
        #vibrate_motor("left")
        
        vibrate.start_vibrate('left', 50, 3)

    

def vibrate_motor(direction):
    
    if direction == 'left':

        print("left motor running")
    
        #GPIO.output(18,True)
        #time.sleep(2)
        
        motorLeft_Pulse(50,3)

    if direction == 'right':

        print("right motor running")
    
        #GPIO.output(23,True)
        #time.sleep(2)
        motorRight_Pulse(100,2)

def motorLeft_Pulse(intensity, num):
    for x in range(num):
        print("motor left pulse")
        
        motorLeft.ChangeDutyCycle(intensity)
        time.sleep(1)
        motorLeft.ChangeDutyCycle(0)
        time.sleep(1)
        

def motorRight_Pulse(intensity, num):
    for x in range(num):
        print("motor right pulse")
        
        motorRight.ChangeDutyCycle(intensity)
        time.sleep(1)
        motorRight.ChangeDutyCycle(0)
        time.sleep(1)
        
        """





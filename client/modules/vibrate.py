# -*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time
import sys

motorleft = None
motorRight = None

sys.path.append('/home/pi/reverb/usb_4_mic_array')
import DOA


URGENT_STRENGTH = 100
LOW_STRENGTH = 60
HIGH_STRENGTH = 80


    
    
def retrieve_from_DOA(strength):
    doa = DOA.main()
    if (doa < 90 and doa >= 0) or (doa >= 300):
        print("RIGHT SIDE: " + str(doa))
        #return ("right")
        
        #vibrate_motor("right")
        if (strength == 'urgent'):
            start_vibrate('both', URGENT_STRENGTH, URGENT_STRENGTH, 0.5, 0.2, 3)
        
        elif (strength == 'low'):
            
            start_vibrate('right', LOW_STRENGTH, LOW_STRENGTH, 1, 1, 2)
            
        else:
            start_vibrate('right', HIGH_STRENGTH, HIGH_STRENGTH, 0.5, 0.5, 3)
            
        
    elif (doa >= 90 and doa < 240):
        print ("LEFT SIDE: " + str(doa))
        #return("left")
        #irection, intensityLeft, intensityRight, duration, interval, num)
        #vibrate_motor("left")
        if (strength == 'urgent'):
           start_vibrate('both', URGENT_STRENGTH, URGENT_STRENGTH, 0.5, 0.2, 3)
        
        elif (strength == 'low'):
            
            start_vibrate('left', LOW_STRENGTH, LOW_STRENGTH, 1, 1, 2)
            
        else:
            start_vibrate('right', HIGH_STRENGTH, HIGH_STRENGTH, 0.5, 0.5, 3)
    else:
        print ("BACK SIDE: " + str(doa))
        if (strength == 'urgent'):
            start_vibrate('both', URGENT_STRENGTH, URGENT_STRENGTH, 0.5, 0.2, 3)
            #start_vibrate('right', URGENT_STRENGTH, 5, 1)
        
        elif (strength == 'low'):
            
            start_vibrate('both', LOW_STRENGTH, LOW_STRENGTH, 1, 1, 2)
            #start_vibrate('right', LOW_STRENGTH, 1, 2)
            
        else:
            start_vibrate('both', HIGH_STRENGTH, HIGH_STRENGTH, 0.5, 0.2, 3)
            #start_vibrate('right', HIGH_STRENGTH, 0.5, 3)
            

def retrieve_from_DOA_degree(strength):
    doa = DOA.main()
    return ('doa: ' + str(doa))
    
    if (strength == 'urgent'):
        print("urgent")
        start_vibrate('both', URGENT_STRENGTH, URGENT_STRENGTH, 0.5, 0.2, 3)
            #start_vibrate('right', URGENT_STRENGTH, 5, 1)
    else:
        print("normal. DOA: " + str(doa))
        if (doa >= 0 and doa <=180):
            degree_left = abs(doa/180 * 100)
            degree_right = abs((180 - doa)/180 * 100)
            #strength_left = int(degree_left * 100)
            print("degree_left: " + str(degree_left))
            #strength_right = int(degree_right * 100)
            print("degree_right: " + str(degree_right))
            
            
            if (degree_left > degree_right):
                strength_left = 100
                strength_right = (degree_right)/(degree_left) * 100
            else:
                strength_right = 100
                strength_left = (degree_left)/(degree_right) * 100
            
            #strength_left = int(degree_left * 100)
            print("strength_left: " + str(strength_left))
            #strength_right = int(degree_right * 100)
            print("strength_right: " + str(strength_right))
            
            start_vibrate('both', strength_left, strength_right, 1, 1, 2)
            #start_vibrate('right', strength_right, 0.5, 1)
        else:
            degree_left = abs((360-doa)/180 * 100)
            degree_right = abs((doa-180)/180 * 100)
            #strength_left = int(degree_left * 100)
            print("degree_left: " + str(degree_left))
            #strength_right = int(degree_right * 100)
            print("degree_right: " + str(degree_right))
            
            if (degree_left > degree_right):
                strength_left = 100
                strength_right = (degree_right)/(degree_left) * 100
            else:
                strength_right = 100
                strength_left = (degree_left)/(degree_right) * 100
            
            start_vibrate('both', strength_left, strength_right, 1, 1, 2)
            #start_vibrate('right', strength_right, 0.5, 1)

def start_vibrate(direction, intensityLeft, intensityRight, duration, interval, num):
    
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
        vibrate_motor(direction, intensityLeft, intensityRight, duration, interval, num)
    
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("Keyboard interrupt")

    finally:
        motorLeft.stop()
        motorRight.stop()
        motorLeft = None
        motorRight = None
        GPIO.cleanup() # cleanup all GPIO
        print("clean up")
    
            

def vibrate_motor(direction, intensityLeft, intensityRight, duration, interval, num):
    
    if direction == 'left':

        print("left motor running")
    
        motorLeft_Pulse(intensityLeft, duration, interval, num)

    elif direction == 'right':

        print("right motor running")
    
        motorRight_Pulse(intensityRight, duration, interval, num)
    
    elif direction == 'both':
        
        print('both motors running')
        motorBoth_Pulse(intensityLeft, intensityRight, duration, interval, num)
        

def motorLeft_Pulse(intensity, duration, interval, num):
    for x in range(num):
        print("motor left pulse")
        
        motorLeft.ChangeDutyCycle(intensity)
        time.sleep(duration)
        motorLeft.ChangeDutyCycle(0)
        time.sleep(interval)
        

def motorRight_Pulse(intensity, duration, interval, num):
    for x in range(num):
        print("motor right pulse")
        
        motorRight.ChangeDutyCycle(intensity)
        time.sleep(duration)
        motorRight.ChangeDutyCycle(0)
        time.sleep(interval)
        
        
def motorBoth_Pulse(intensityLeft, intensityRight, duration, interval, num):
    for x in range(num):
        print("both motors  pulse")
        
        motorLeft.ChangeDutyCycle(intensityLeft)
        motorRight.ChangeDutyCycle(intensityRight)
        time.sleep(duration)
        motorLeft.ChangeDutyCycle(0)
        motorRight.ChangeDutyCycle(0)
        time.sleep(interval)
        
        

retrieve_from_DOA_degree('normal')


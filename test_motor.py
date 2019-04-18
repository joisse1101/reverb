
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

# Initial state for LEDs:
print("Testing RF out, Press CTRL+C to exit")

try:
    print('try')
    
    p = GPIO.PWM(18,100)
    p.start(0)
    p1 = GPIO.PWM (23,100)
    p1.start(0)
    
    print("p: " + str(p))
    print("p1: " + str(p1))
         
    for y in range(0,2):
        print('loop')
    
        for x in range(50,110,10):
            print(x)
            p.ChangeDutyCycle(x)
            p1.ChangeDutyCycle(x)
            time.sleep(0.5)
            
            p.ChangeDutyCycle(0)
            p1.ChangeDutyCycle(0)
            time.sleep(0.5)


     
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")

except:
    print("some error") 

finally:
    GPIO.cleanup() # cleanup all GPIO
    print("clean up") 
    
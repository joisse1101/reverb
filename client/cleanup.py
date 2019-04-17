import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

motorLeft = GPIO.PWM(18,100)
motorLeft.start(0)
motorRight = GPIO.PWM(23,100)
motorRight.start(0)

GPIO.cleanup()
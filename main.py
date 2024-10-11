import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

def play_buzzer():
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(13, GPIO.LOW)


play_buzzer()

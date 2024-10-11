import RPi.GPIO as GPIO
from pirc522 import RFID
import signal
import time

rdr = RFID()
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

def play_buzzer():
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(13, GPIO.LOW)


try:
    while True:
        rdr.wait_for_tag()  # Attendre qu'une carte soit à proximité
        (error, tag_type) = rdr.request()

        if not error:
            print("Carte détectée")
            (error, uid) = rdr.anticoll()  # Lecture de l'UID de la carte

            if not error:
                print(f"UID de la carte: {uid}")

                # Appeler la fonction pour jouer le buzzer ici
                play_buzzer()

                # Délai pour éviter la détection multiple
                time.sleep(1)

finally:
    rdr.cleanup()








#GPIO.setmode(GPIO.BCM)
#GPIO.setup(13, GPIO.OUT)




#play_buzzer()
#GPIO.cleanup()
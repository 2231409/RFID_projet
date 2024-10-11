import RPi.GPIO as GPIO
from pirc522 import RFID
import signal
import time

rdr = RFID()
#GPIO.setmode(GPIO.BCM)
GPIO.setup(33, GPIO.OUT)
#GPIO.cleanup()
def play_buzzer():
    GPIO.output(33, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(33, GPIO.LOW)


try:
    while True:
        rdr.wait_for_tag()  # Attendre qu'une carte soit à proximité
        (error, tag_type) = rdr.request()
        print("Tag detected")
        (error, uid) = rdr.anticoll()
        if not error:
            print("UID: " + str(uid))
            # Select Tag is required before Auth
            if not rdr.select_tag(uid):
                # Auth for block 10 (block 2 of sector 2) using default shipping key A
                if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
                    # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    print("Reading block 10: " + str(rdr.read(10)))
                    # Always stop crypto1 when done working
                    rdr.stop_crypto()
        # if not error:
        #     print("Carte détectée")
        #     (error, uid) = rdr.anticoll()  # Lecture de l'UID de la carte
        #
        #     if not error:
        #         print(f"UID de la carte: {uid}")
        #         print()
        #
        #         # Appeler la fonction pour jouer le buzzer ici
        #         play_buzzer()

                # Délai pour éviter la détection multiple
                time.sleep(1)

finally:
    rdr.cleanup()








#GPIO.setmode(GPIO.BCM)
#GPIO.setup(13, GPIO.OUT)




#play_buzzer()
#GPIO.cleanup()
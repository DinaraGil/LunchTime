import RPi.GPIO as GPIO
from mfrc522 importSimpleMFRC522

class Read_card():
    _reader = SimpleMFRC522()

    try:
        card_id = _reader.read()
    finally:
        GPIO.cleanup()
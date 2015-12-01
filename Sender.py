#Sender.py
import Adafruit_BBIO.GPIO as GPIO
from twython import Twython
import requests
GPIO.setup("P8_14", GPIO.IN)
requests.packages.urllib3.disable_warnings()
USER_KEY="User key for twitter app"
USER_SECRET="User Secret for twitter app"
ACCESS_TOKEN="Access token for twitter app"
ACCESS_TOKEN_SEC="Access token secret for twitter app"
client_args = {
    'verify': False
}
twitter=Twython(USER_KEY,USER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SEC,client_args=client_args)

while True:
        if GPIO.input("P8_14"):
                twitter.update_status(status="Detected Sensor output")

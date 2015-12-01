#Receiver.py
from twython import TwythonStreamer
class IoTStreamReader(TwythonStreamer):
def on_success(self, data):
    print "Received Tweet from Sensor:"
    print data
def on_error(self, status_code, data):
    printstatus_code
    self.disconnect()
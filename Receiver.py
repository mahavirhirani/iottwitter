#Receiver.py
from twython import TwythonStreamer
class IoTStreamReader(TwythonStreamer):
def on_success(self, data):
    print "Received Tweet from Sensor:"
    print data
def on_error(self, status_code, data):
    printstatus_code
    self.disconnect()
    
USER_KEY="User key for twitter app"
USER_SECRET="User secret for twitter app"
ACCESS_TOKEN="Access token"
ACCESS_TOKEN_SEC="Access token secret"
client_args = {
 'verify': False
}
stream = IoTStreamReader(USER_KEY, USER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SEC)
stream.statuses.filter(track='Sensor')
 
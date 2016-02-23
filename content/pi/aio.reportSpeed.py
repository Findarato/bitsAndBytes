#!/usr/bin/python

from Adafruit_IO import *
import subprocess
import os
import re
import time

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = ""

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)
result = []

# We need to call the speed test
#display out put line by line

#filters output
proc = subprocess.Popen(["/usr/local/bin/speedtest-cli --simple --secure"],stdout=subprocess.PIPE,shell="/bin/bash")
while True:
  line = proc.stdout.readline()
  if line != '':
    #the real code does filtering here
    value = re.findall('\\b\\d+\\b', line.rstrip())
    s = "."
    result.append(s.join(value))
  else:
    break

# Displaying the data for debug. This can be removed or commented out
# None of this is actually needed for logging with Adafruit, it is debug.
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime
print "Sent Ping:",result[0]
print "Sent Download:",result[1]
print "Sent Upload:",result[2]
# End Debug


#Actually Sending The data
aio.send('speed-test-ping', result[0])
aio.send('download', result[1])
aio.send('upload', result[2])

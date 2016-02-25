sudo pip install git+https://github.com/sivel/speedtest-cli.git
sudo pip install adafruit-io

#Enter one of the two into crontab. These are setup for the raspberry pi
# 0 * * * *  /usr/bin/python /home/pi/python/aio.reportSpeed.py >> /home/pi/python/reportSpeed.txt 2>&1
# */30 * * * *  /usr/bin/python /home/pi/python/aio.reportSpeed.py >> /home/pi/python/reportSpeed.txt 2>&1

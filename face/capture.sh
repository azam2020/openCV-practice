
#!/bin/bash
DATE=$(date +"%Y-%m-%d-%H-%M")
cd /home/pi/Azam/face_recognition
fswebcam -r 1920x1080 -p YUYV -s 30 -D 2 -F 2 --no-banner  /home/pi/Azam/face_recognition/capturepics/$DATE.jpg
cp /home/pi/Azam/face_recognition/capturepics/$DATE.jpg /home/pi/Azam/face_recognition/latest.jpg
python3 weather.py
#./weatherftp.sh

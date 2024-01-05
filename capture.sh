
#!/bin/bash
DATE=$(date +"%Y-%m-%d-%H-%M")
fswebcam -r 1920x1080 -p YUYV -s 30 -D 2 -F 2 --no-banner  /home/pi/Azam/openCV/capturepics/$DATE.jpg


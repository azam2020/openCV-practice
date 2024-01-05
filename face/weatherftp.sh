
#!/bin/bash
host = master
user="Azam"
password="Azam@123"

lftp $host -e "set ssl:verify-certificate false;"<<EOF
user $user $password
cd geek-and-gamer.com/webcam
mput weatherwebcam.jpg
bye
EOF

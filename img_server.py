from flask import Flask, render_template, request
from PIL import Image
import cv2
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

@app.route('/upload', methods=['POST'])
def img_face_recognition():
	if 'image' in request.files:
		uploaded_image = request.files['image']
		temp_path = 'temp.jpg'
		uploaded_image.save(temp_path)
		img = cv2.imread(temp_path)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow('Image',img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		#return render_template('index.html',message="Done")

@app.route('/webcam')
def webcam_face_recognition():
	subprocess.run(['python3', 'data.py'])	
	return render_template('index.html')

@app.route('/labelled_webcam')
def labelled_webcam_face_recognition():
	subprocess.run(['python3', 'label.py'])
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True, port=5000)


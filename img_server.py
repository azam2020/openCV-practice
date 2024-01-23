from flask import Flask, render_template, request
from PIL import Image
import cv2
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def img_face(temp_path):
	print("Image face detection function")
	img = cv2.imread(temp_path)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
	for (x,y,w,h) in faces:
	        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	dw = 1300
	h,w = img.shape[:2]
	r = h/w
	dh = int(r*dw)
	img = cv2.resize(img,(dw,dh))
	#cv2.imshow('Image',img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

def video_face():
	print("video-face function called")
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	cap = cv2.VideoCapture('uploaded_video.avi')
	while(True):
		ret, frame = cap.read()
		if not ret:
			break
		gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow('Frame',frame)
		if cv2.waitKey(35) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

@app.route('/upload', methods=['POST'])
def img_face_recognition():
	if 'image' in request.files:
		print("image uploaded")
		uploaded_image = request.files['image']
		if uploaded_image.filename=='':
			return render_template('index.html',message="No file selected")

		temp_path = 'temp.jpg'
		uploaded_image.save(temp_path)
		img_face(temp_path)
		return render_template('index.html')

@app.route('/video_upload',methods=['POST'])
def video_face_recognition():
        if 'video' in request.files:
                print("video uploaded")
                uploaded_video = request.files['video']
                if uploaded_video.filename=='':
                        return render_template('index.html',message="No file selected")
                uploaded_video.save('uploaded_video.avi')
                video_face()
                return render_template('index.html')



@app.route('/webcam',methods=['POST'])
def webcam_face_recognition():
	name = request.form['input_name']
	if name=='':
		name="unknown"
	print("Webcam program is running")
	subprocess.run(['python3', 'dataset.py', name])
	return render_template('index.html')

@app.route('/play_video')
def play_video():
	cap = cv2.VideoCapture('latest.avi')
	if(cap.isOpened()==False):
		print("No file named latest.avi")
		return render_template('index.html',message="First open webcam to record your video")
	else:
		while(cap.isOpened()):
			ret,frame = cap.read()
			if ret:
				cv2.imshow('Video',frame)
				if cv2.waitKey(45) & 0xFF ==ord('q'):
					break
			else:
				break

		cap.release()
		cv2.destroyAllWindows()
		subprocess.run(['rm', 'latest.avi'])
		return render_template('index.html')

@app.route('/picture')
def click_picture():
	subprocess.run(['fswebcam','-r','1920x1080','-p','YUYV','-s','30','-D','5','-F','2','--no-banner','clicked-pic.jpg'])
	#return render_template('index.html',message="Please look towards the camera for picture.")
	#path = 'capturepics/latest.jpg'
	img_face("clicked-pic.jpg")
	return render_template('index.html',message="Picture Clicked......!!")
@app.route('/labelled_webcam')
def labelled_webcam_face_recognition():
	subprocess.run(['python3', 'label.py'])
	print("Labelled-webcam program is runnig")
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True, port=5000)


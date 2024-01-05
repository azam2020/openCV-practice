from flask import Flask, render_template, request
import cv2

app = Flask(__name__)
@app.route('/')
def display_result():
	# Load pre-trained face detection model
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	# Load the image
	img = cv2.imread('azam.jpg')

	# Convert image to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
	# Draw rectangles around the detected faces
	for (x, y, w, h) in faces:
    		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# Display the result
	#cv2.imshow('Face Recognition', img)
	return render_template('index.html', result=img)
	#cv2.waitKey(0)  # Waits for a key press to close the window
	#cv2.destroyAllWindows()


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5002,debug=True)

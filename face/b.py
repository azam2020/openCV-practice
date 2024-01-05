from flask import Flask, render_template, request
import cv2

app = Flask(__name__)
@app.route('/')
def display_result():
	#img_url = url_for('static', filename='azam.jpg')
	img_url = '/static/azam.jpg'
	return render_template('index.html', result = img_url)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5002,debug=True)

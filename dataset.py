import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

skip = 0
face_data = []

dataset_path = "./face_dataset/"

if len(sys.argv)<2:
	print("Enter your name as command line argument.")
	sys.exit(1)
file_name = sys.argv[1]

#Record at the same time
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('latest.avi',fourcc,25.0,(640,480))



while True:
    ret, frame = cap.read()

    if not ret:
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        continue
    faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
    skip += 1

    for face in faces[:1]:
        x, y, w, h = face
        offset = 5
        face_offset = frame[y - offset : y + h + offset, x - offset : x + w + offset]
        face_selection = cv2.resize(face_offset, (100, 100))

        if skip % 10 == 0:
            face_data.append(face_selection.flatten())

        cv2.rectangle(frame, (x, y), (x + w, y + h), (8, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Faces", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

face_data = np.array(face_data)

face_data = face_data.reshape((face_data.shape[0],-1))

if file_name != "unknown":
	np.save(dataset_path + file_name, face_data)
	print(f"Data saved as {file_name}.avi")
print("Data not saved. Reason: name not entered")
print("Video recorded as latest.avi")
cap.release()
out.release()
cv2.destroyAllWindows()

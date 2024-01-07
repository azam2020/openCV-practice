import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import os

def load_dataset(dataset_path):
    face_data = []
    labels = []

    for filename in os.listdir(dataset_path):
        if filename.endswith(".npy"):
            data = np.load(os.path.join(dataset_path, filename))
            label = filename[:-4]  # Remove the '.npy' extension
            #data_flattened = data.flatten()
            face_data.append(data)
            labels.extend([label] * len(data))
		
    face_data = np.concatenate(face_data, axis=0)
    #print(face_data)
    return face_data, labels

def predict_person(face_data, labels, test_face):
    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    test_face_flattened = test_face.flatten()
    knn_classifier.fit(face_data, labels)
    predicted_label = knn_classifier.predict([test_face_flattened])[0]
    return predicted_label

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

dataset_path = "./face_dataset/"
file_name = input("Enter the name of the person: ")
face_data, labels = load_dataset(dataset_path)

new_face_data = []
skip = 0

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
        face_offset = frame[y:y+h, x:x+w]
        test_face = cv2.resize(face_offset, (100, 100))
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (8, 255, 0), 2)
        
        if test_face.flatten() in face_data:
            predicted_label = predict_person(face_data, labels, test_face)
            cv2.putText(frame, predicted_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2, cv2.LINE_AA)
        elif skip%10==0 and test_face.flatten() not in face_data:
                new_face_data.append(test_face.flatten())
                #cv2.putText(frame, "unknown_person", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2, cv2.LINE_AA)
                
    cv2.imshow("Face Recognition", frame)
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

if file_name not in labels:
    new_face_data = np.array(new_face_data)
    new_face_data = new_face_data.reshape((new_face_data.shape[0],-1))
    np.save(dataset_path + file_name, new_face_data)

cap.release()
cv2.destroyAllWindows()

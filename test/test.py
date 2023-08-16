# model testing file

import cv2 
import numpy as np 
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import os 


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# models we are using 
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
classifier = load_model("model.h5")
print("Imports and models loaded!!!")

# labels on which we trained the model 
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

print(f"labels we are working on: {emotion_labels}")

# Load the image
image_path = 'test.png'  # Replace with the actual image path
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w]
    roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

    if np.sum([roi_gray]) != 0:
        roi = roi_gray.astype('float') / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        prediction = classifier.predict(roi)[0]
        label = emotion_labels[prediction.argmax()]
        print("Emotion:", label)
    else:
        print("No Faces Detected")

cv2.destroyAllWindows()
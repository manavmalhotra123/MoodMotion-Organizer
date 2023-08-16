import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
classifier = load_model("emotion_classifier/model.h5")

def classify_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi_gray = cv2.resize(gray, (48, 48), interpolation=cv2.INTER_AREA)
    
    if np.sum([roi_gray]) != 0:
        roi = roi_gray.astype('float') / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        prediction = classifier.predict(roi)[0]
        emotion_index = prediction.argmax()
        emotion = emotion_labels[emotion_index]
        return emotion
    else:
        return "Unknown"
import os
import cv2
from classifier import classify_emotion

def process_video(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    emotions = []
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_number % fps == 0:
            emotion = classify_emotion(frame)
            emotions.append(emotion)
        
        frame_number += 1
    
    cap.release()
    
    most_common_emotion = max(set(emotions), key=emotions.count)
    output_subfolder = os.path.join(output_folder, most_common_emotion)
    
    if not os.path.exists(output_subfolder):
        os.makedirs(output_subfolder)
    
    output_video_path = os.path.join(output_subfolder, os.path.basename(video_path))
    os.rename(video_path, output_video_path)
    
    print(f"Processed {output_video_path} - Emotion: {most_common_emotion}")

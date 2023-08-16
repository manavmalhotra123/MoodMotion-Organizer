import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Extract one frame per second
        if frame_number % fps == 0:
            output_file = os.path.join(output_folder, f"frame_{frame_number}.jpg")
            cv2.imwrite(output_file, frame)
            print(f"Extracted {output_file}")

        frame_number += 1

    cap.release()

if __name__ == "__main__":
    video_path = "video.mp4"  # Replace with your video file's path
    output_folder = "output_frames"  # Replace with the desired output folder

    extract_frames(video_path, output_folder)

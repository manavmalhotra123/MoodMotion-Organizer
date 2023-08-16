import os
from video_processor import process_video
from classifier import emotion_labels

def main():
    video_folder = "input_videos"  # Replace with the folder containing video files
    output_folder = "output_videos"  # Replace with the desired output folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):  # Adjust the file extension if needed
            video_path = os.path.join(video_folder, video_file)
            process_video(video_path, output_folder)

if __name__ == "__main__":
    main()

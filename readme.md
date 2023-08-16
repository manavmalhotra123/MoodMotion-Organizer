Absolutely, here's an updated version of the README file with added usage examples:

```markdown
# MoodMotion Organizer

MoodMotion Organizer is a Python tool that automates the process of organizing video files based on their most frequent emotion. This project utilizes facial emotion recognition to classify emotions in videos and then sorts them into folders based on the dominant emotion.

## Features

- Efficiently extracts frames from video files.
- Utilizes an emotion classification model for accurate emotion recognition.
- Organizes video files into separate folders named after the most frequent emotion.

## Getting Started

These instructions will help you set up and run the MoodMotion Organizer project on your local machine.

### Prerequisites

- Python 3.x
- OpenCV
- Keras

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/moodmotion-organizer.git
   cd moodmotion-organizer
   ```

2. Install the required packages using pip:

   ```bash
   pip install opencv-python keras
   ```

3. Place your `model.h5` and `haarcascade_frontalface_default.xml` files in the project directory.

### Usage

1. Place the video files you want to organize in the `test` directory.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The tool will process each video, classify emotions, and organize them into subfolders based on the most frequent emotion.

### Examples

- **Family Memories:** Organize your family vacation videos based on the predominant emotions captured in each video. Easily find and watch joyful, exciting, or emotional moments.

- **Media Collection:** Manage your movie or TV show collection by categorizing videos into folders like "Action," "Drama," "Comedy," etc., based on the emotions portrayed in the scenes.

- **Video Logs:** If you're a vlogger, sort your video logs based on the primary mood of each recording. Quickly locate and share the moments that match your desired emotional tone.

### Structure

- `classifier.py`: Emotion classification module.
- `haarcascade_frontalface_default.xml`: Haarcascade XML file for face detection.
- `main.py`: Main script to run the MoodMotion Organizer tool.
- `model.h5`: Emotion classification model.
- `test/`: Folder containing individual testing files for each module.
   - `framecapture.py`: Script for capturing frames from videos.
   - `test.png`: Test image for classification.
   - `test.py`: Test script for the classifier.
   - `video.mp4`: Sample video file for testing.
- `video_processor.py`: Video processing module.

### Credits
- Haarcascade XML file for face detection.

## Acknowledgments

- The emotion classification model is based on dataset provided on link [https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset]


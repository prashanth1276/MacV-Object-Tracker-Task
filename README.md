# MacV-Object-Tracker-Task

This project demonstrates the process of tracking multiple objects in a video using **OpenCV** and the **CSRT Tracker**. The project includes real-time tracking with the ability to select multiple objects and generate trails for each object as they move through the video frames.

## Features
- **Multiple Object Tracking**: Select and track multiple objects in a video.
- **Bounding Boxes and Centroids**: Each tracked object is represented by a bounding box and centroid.
- **Object Trails**: Trails are drawn for each object, showing the path they have traveled.
- **Output Video**: The processed video is saved with the tracked objects and their respective trails.
- **Customizable Object Selection**: Users can select the objects they want to track during the initialization phase.

## Requirements

- Python 3.x
- OpenCV
- opencv-python
- opencv-contrib-python
- NumPy

## Installation
## Install dependencies using pip:
- pip install -r requirements.txt

## How to Use
1. Input Video: Place the video you want to track objects in the assets folder.
2. Run the Code: Run the main Python script:
   - python tracker.py
3. Object Selection: When the video opens, a window will appear where you can select multiple objects to track. Click and drag to define the Region of Interest (ROI). If done with selection the click Enter / Space to stop selection and run. If you wish to exit then click Esc.
4. Result: After object selection, the script will begin tracking the objects and display the bounding boxes, centroids, and trails for each object in real-time. The processed video with all the tracking information will be saved as output_video.mp4 in the output folder.

## Project Structure
### MacV_Object_Tracker
1. assets/
   MacV.mp4         # Input video file for tracking
2. output/
   output_video.mp4         # Output video with object tracking
3. src/
   tracker.py           # Main script for object tracking
   utils.py        # Helper function to draw the trail of tracked objects
4. web/
   index.html          # Web page to display the result video in the browser
5. requirements.txt       # List of dependencies
6. README.md          # Project documentation

## Code Explanation
1. tracker.py
  -> This is the main script that performs object tracking. It includes:
   
    1. Video Capture: Captures video frames from the input video.
    2. Object Selection: Uses OpenCV's selectROIs to allow users to select multiple objects in the first frame.
    3. CSRT Tracker: Uses OpenCV's CSRT tracker to track the objects throughout the video.
    4. Centroid and Trail: For each object, the centroid is calculated, and its trail is drawn across the video frames.
    5. Output Video: The processed frames are saved to an output video file.
   
3. utils.py
   -> This utility function is responsible for drawing the trails of the tracked objects in the video. It takes the list of centroids for each object and draws lines connecting them to create a visual trail.

## Result Video
click the link to view the video directly in the repository:

[Watch the result video](assets/result_video.mp4)

# Lane Detector

## Overview
This project implements a lane detection system using OpenCV's Hough Line Transform and edge detection techniques. It processes video frames to identify lanes in real-time, highlighting detected lane lines using red overlays.

## Features
- **Edge Detection**: Uses Canny edge detection for identifying lane boundaries.
- **Morphological Operations**: Applies a top-hat morphological transformation to enhance edges and suppress noise.
- **Hough Line Transform**: Detects line segments representing lane boundaries.
- **Slope Filtering**: Filters out lines based on slope values to ensure only valid lane lines are detected.
- **Dynamic Overlay**: Draws detected lanes directly on the video frames for visualization.

## Dependencies
- OpenCV
- NumPy

## Usage
### Run the Lane Detector
```bash
python lane_detector.py
```

### Input Video
Replace 'Demo.mp4' with your desired input video by updating the path in the script.

## Code Structure
### lane_detector.py
- **Video Input**: Reads frames from a video file ('Demo.mp4') and processes them continuously.
- **Thresholding**: Converts frames to grayscale and applies binary thresholding to highlight lane regions.
- **Edge Detection**: Uses Canny edge detection with thresholds to extract edges.
- **Top-Hat Filtering**: Enhances edges using morphological operations to suppress noise.
- **Hough Line Detection**: Identifies line segments and filters based on slope and length to detect lanes.
- **Visualization**: Draws detected lanes in red on the original video frames for display.

## Key Functions
- **top_hat(val, size)**: Applies a morphological top-hat filter to enhance image contrast and suppress background noise.
- **Canny Edge Detection**: Extracts edges from thresholded frames for processing.
- **HoughLinesP**: Detects lines using the probabilistic Hough Transform.
- **Slope Filtering**: Filters lines based on slope to retain valid lanes and excludes noise.

## Notes
- Press 'Q' to quit the application while the video is running.
- Adjust thresholds and parameters in the code for optimal performance based on the input video.

### Example Output
The output displays detected lanes highlighted in red over the original video frames.

#  Run
 ```bash
 python lane_detector.py
 ```
# Demo

![dst](https://user-images.githubusercontent.com/48129098/115986568-61afc300-a5e3-11eb-8e3e-d95df858860d.gif)
![thres_concat](https://user-images.githubusercontent.com/48129098/115986342-4f815500-a5e2-11eb-91d8-e286aa25a547.gif)
![thres](https://user-images.githubusercontent.com/48129098/115986355-5a3bea00-a5e2-11eb-966c-ed4a8cdcb9c5.gif)
![edge](https://user-images.githubusercontent.com/48129098/115986358-5e680780-a5e2-11eb-86fc-1c4caa5c54ce.gif)


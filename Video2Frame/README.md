# Video Frame Extractor

This Python script provides a utility to extract frames from a video file at regular intervals.

## Features

- Extracts frames from a specified video file.
- Saves extracted frames to a designated output directory.
- Allows specification of the interval between frames to be saved.

## Requirements

The script requires Python 3 and the following library:
- `opencv-python` (cv2): For video processing functions.

## Results
I have saved all extracted frames in the `All_Frames` folder. Here's an example of an output image:

![Result Image](All_Frames/image1.jpg)

## Custom Dataset
I designed this script to facilitate the creation of custom datasets by allowing adjustable frame intervals. For example, the function can be set up as follows:

```python
def extract_frames(video_path, output_dir, frame_interval=1):
```

## Running the Container
To run the Docker container with the default settings, execute the following command in your terminal:
```bash
docker-compose up --build
```

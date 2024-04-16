# Detect and Track Bubbles

This project focuses on tracking bubbles, ensuring each bubble is uniquely identified and tracked accurately, even when other bubbles intersect or overlap with it. The implementation uses YOLOv9 for object detection, and the system is Dockerized to facilitate easy setup and deployment.

## Project Overview

- **Custom Dataset**: Created using ROBOFLOW for annotation, with custom augmentations to enhance model accuracy.
- **Model Training**: Utilized YOLOv9 trained on a custom dataset to achieve precise object detection.
- **Deployment**: Dockerized environment for easy and consistent deployment across different systems.

## Custom Dataset Creation

I developed my own dataset, annotating it with YOLOv9 format using ROBOFLOW, resulting in 31 annotated images.

![Roboflow Images](ReadMe_Images/Roboflow_Img.png)

Post annotation, I applied custom augmentations to improve the model's robustness.

![Roboflow Custom Dataset](ReadMe_Images/Roboflow_Img2.png)

The dataset was finalized and versioned on April 9, 2024.

![ROBOFLOW V1](ReadMe_Images/Roboflow_Img3.png)

## Training YOLOv9

For training YOLOv9 on the custom dataset, follow the detailed guide in this notebook:

[How to Train YOLOv9 on a Custom Dataset](https://github.com/roboflow/notebooks/blob/main/notebooks/train-yolov9-object-detection-on-custom-dataset.ipynb)

### Setup and Installation

Due to a known issue in the original YOLOv9 repository, use the following fork which contains a necessary patch:

```bash
git clone https://github.com/SkalskiP/yolov9.git
cd yolov9
pip install -r requirements.txt -q
```

### Authenticate and Download the Dataset

I used this code to Connect to and download the custom dataset from Roboflow. I used my version(1): 
```bash
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="5gekjLhYgxZ9u4KnCJGz")
project = rf.workspace("isu-cede4").project("dot_track_vid")
version = project.version(1)
dataset = version.download("yolov9")
```

### Training Results
By default, the results of each subsequent training sessions are saved in {HOME}/yolov9/runs/train/, in directories named exp, exp2, exp3

I put my runs directory in the utils folder and the results save in the exp2.

![Result Image](utils/runs/train/exp2/train_batch2.jpg)
![Result Image](utils/runs/train/exp2/results.png)
![Result Image](utils/runs/train/exp2/val_batch0_pred.jpg)

## Bubble Detection and Tracking
Now by the Docker When you run the main.py in the src folder. For the circle detection I define the X1, Y1, X2, Y2. By this locations I define the circle center and radios and add the circles to the frame. I log the circles location in the txt file also.

### Video Output
![Circles Locations](ReadMe_Images/output.gif)

### Circles Locations Logs
![Circles Locations](ReadMe_Images/Circles_Locations.png)


## Running the Container
To run the Docker container with the default settings, execute the following command in your terminal:
```bash
docker-compose up --build
```

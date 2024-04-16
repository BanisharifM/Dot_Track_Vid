import cv2
import torch
import math
from IPython.display import Video

# Load the trained YOLOv9 model
model = torch.hub.load("yolov9", "custom", path="models/best.pt", source="local")


# Function to process and display the video
def process_video(input_video_path, output_video_path, coords_output_path):
    # Capture the video
    cap = cv2.VideoCapture(input_video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Prepare to write bubble locations
    with open(coords_output_path, "w") as file:
        frame_count = 0

        header = "\t".join([f"Frame no.", *[f"Bubble_{i+1}" for i in range(10)]])
        file.write(header + "\n")

        while cap.isOpened():
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Perform detection
                results = model(frame)

                # Sort detections based on the x-coordinate of the center
                sorted_detections = sorted(
                    results.xyxy[0], key=lambda det: (det[0] + det[2]) / 2
                )

                # Prepare text file content for this frame
                bubble_info = [f"Frame {frame_count}"]

                # Extract data, draw ellipses, and label them
                for i, detection in enumerate(
                    sorted_detections[:10]
                ):  # Limit to the first 10 detections
                    x1, y1, x2, y2, conf, cls = detection
                    x1 = x1.item()  # Convert tensor to float
                    y1 = y1.item()  # Convert tensor to float
                    x2 = x2.item()  # Convert tensor to float
                    y2 = y2.item()  # Convert tensor to float
                    center_x = (x1 + x2) / 2
                    center_y = (y1 + y2) / 2
                    circle_r_x = int((x2 - x1) / 2)
                    center = (
                        int(round(center_x)),
                        int(round(center_y)),
                    )  # Use round after converting tensor values to floats
                    cv2.circle(frame, center, circle_r_x - 5, (255, 0, 0), 2)
                    cv2.putText(
                        frame,
                        str(i + 1),
                        center,
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )

                    # Add coordinate information
                    bubble_info.append(f"({int(center_x)}, {int(center_y)})")
                    # bubble_info.append(f"Bubble_{i + 1} ({center[0]}, {center[1]})")

                # Write the frame
                out.write(frame)

                # Write bubble info to the text file
                # file.write(" ".join(bubble_info) + "\n")
                # Add empty entries if less than 10 detections
                while len(bubble_info) < 11:
                    bubble_info.append("")

                # Write the frame data in tab-separated format
                file.write("\t".join(bubble_info) + "\n")

                frame_count += 1

    # Release everything when done
    cap.release()
    out.release()


# Process the video
process_video(
    "Dot_Track_Vid_2024_fall.mp4", "results/output.mp4", "results/bubble_locations.txt"
)

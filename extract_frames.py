import cv2
import os


def extract_frames(video_path, output_dir, frame_interval=5):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_count = 0
    image_count = 1

    while True:
        # Read a frame
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Save every 'frame_interval' frame
        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_dir, f"image{image_count}.jpg")
            cv2.imwrite(output_path, frame)
            image_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {image_count - 1} frames from {video_path}")


# Example usage
extract_frames("data/Videos/Dot_Track_Vid_2024_fall.mp4", "Custom_Dataset")

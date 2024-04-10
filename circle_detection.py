import cv2
import numpy as np
import os

# Create a directory to save the result images
output_dir = "results/"
os.makedirs(output_dir, exist_ok=True)

# Load the image
image = cv2.imread("data/Images/image1.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circles using HoughCircles
# Adjust the parameters as needed for your specific video
circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=30,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=100,
)

# Draw and number the detected circles
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i, circle in enumerate(circles[0, :], start=1):
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)
        cv2.circle(image, center, 2, (0, 0, 255), 3)
        cv2.putText(
            image, str(i), center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2
        )

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Save the result
output_path = os.path.join(output_dir, "detected_circles5.jpg")
cv2.imwrite(output_path, image_rgb)

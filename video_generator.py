import os
import cv2

# Define the directory containing the images and the output video file
image_dir = "downloaded_images"
output_video = "output_video.mp4"
fps = 30  # Frames per second

# Get the list of image files
image_files = sorted([img for img in os.listdir(image_dir) if img.endswith(".jpg") or img.endswith(".png")])

# Check if there are any images in the directory
if not image_files:
    print(f"No images found in directory {image_dir}")
    exit()

# Read the first image to get the frame size
first_image_path = os.path.join(image_dir, image_files[0])
first_image = cv2.imread(first_image_path)
if first_image is None:
    print(f"Failed to read the first image from {first_image_path}")
    exit()

frame_height, frame_width, _ = first_image.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4
video_writer = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

# Process each image and add it to the video
for idx, image_file in enumerate(image_files):
    image_path = os.path.join(image_dir, image_file)
    print(f"Processing {idx + 1}/{len(image_files)}: {image_path}")
    image = cv2.imread(image_path)
    if image is not None:
        if image.shape[1] != frame_width or image.shape[0] != frame_height:
            print(f"Resizing image from {image.shape[1]}x{image.shape[0]} to {frame_width}x{frame_height}")
            image = cv2.resize(image, (frame_width, frame_height))
        video_writer.write(image)
    else:
        print(f"Skipping {image_path} due to read error")

# Release the VideoWriter object
video_writer.release()
print(f"Video saved as {output_video}")
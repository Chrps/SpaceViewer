import os
import requests

# Specify the path to the list of files and the directory to save images
input_file = "found_files.txt"
output_dir = "downloaded_images"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to download and save an image
def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Saved: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Read the list of image URLs from the input file
with open(input_file, 'r') as file:
    urls = file.readlines()

# Download each image and save it to the output directory
for idx, url in enumerate(urls):
    url = url.strip()  # Remove any surrounding whitespace or newline characters
    if url:
        filename = os.path.basename(url)
        save_path = os.path.join(output_dir, filename)
        print(f"Downloading {idx + 1}/{len(urls)}: {url}")
        download_image(url, save_path)

print(f"\nAll images have been downloaded to {output_dir}")
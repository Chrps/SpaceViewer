import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import time

base_url = "https://sdo.gsfc.nasa.gov/assets/img/browse/2024/01/"
date_paths = [f"{base_url}{str(i).zfill(2)}/" for i in range(1, 32)]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_files(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all links ending with 1024_HMIIF.jpg
    start_time = time()
    print(len(soup.find_all('a', href=True)))
    print(f"Time taken: {time() - start_time}")

    '''for a in soup.find_all('a', href=True):
        href = a['href']
        if href.endswith('1024_HMIIF.jpg'):
            full_url = urljoin(url, href)
            files.append(full_url)
    
    return files'''

all_files = []
total_dates = len(date_paths)
for idx, path in enumerate(date_paths):
    print(f"Processing {idx + 1}/{total_dates}: {path}")
    get_files(path)
    #print(f"Found {len(files)} files in {path}")
    #all_files += files

# Print the total number of files found
'''print(f"\nTotal files found: {len(all_files)}\n")

# Save the list of files to a file
output_file = "found_files.txt"
with open(output_file, 'w') as f:
    for file in all_files:
        f.write(file + "\n")

print(f"\nTotal files found: {len(all_files)}")
print(f"List of files saved to {output_file}")'''
import concurrent.futures
import os
import re
from multiprocessing import freeze_support
import instaloader
import pandas as pd
import tqdm

# Function to extract shortcode from a given URL
def extract_shortcode(url):
    match = re.search(r'\/[a-zA-Z0-9_-]+\/([a-zA-Z0-9_-]+)\/', url)
    return match.group(1) if match else None

# Function to download Instagram videos
def download_instagram_video(url, loader, download_folder):
    shortcode = extract_shortcode(url)
    if not shortcode:
        print(f"Skipped {url} - Invalid URL format.")
        return

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        if post.typename == 'GraphVideo':
            loader.download_post(post, target=download_folder)
            print(f"Downloaded video from {url}")
        else:
            for sidecar_node in post.get_sidecar_nodes():
                if sidecar_node.is_video:
                    video_url = sidecar_node.video_url
                    loader.download_post(post, target=download_folder)
                    print(f"Downloaded video from {url}")
                    return  # Early return if a video is found
            print(f"Skipped {url} - No videos found.")
    except Exception as e:
        print(f"Skipped {url} - Error during download: {str(e)}")

# Function to handle the login process
def login(loader):
    while True:
        username = input("Instagram username: ")
        password = input("Instagram password: ")
        try:
            loader.login(username, password)
            loader.save_session_to_file()
            print("Login successful!")
            break
        except instaloader.exceptions.InstaloaderException as e:
            print(f"Login error: Please try again.")

if __name__ == '__main__':
    freeze_support()
    # Creating an instaloader object
    loader = instaloader.Instaloader()
    # Handling the login process
    login(loader)

    # Reading addresses from an Excel file
    excel_file = "instagram.xlsx"
    df = pd.read_excel(excel_file)
    urls = df['Links'].tolist()

    # Removing duplicate addresses
    unique_urls = list(set(urls))

    # Creating a download folder
    download_folder = "Downloads"
    os.makedirs(download_folder, exist_ok=True)

    # Using multi-processing to iterate through addresses and download videos
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        results = list(tqdm.tqdm(executor.map(download_instagram_video, unique_urls, [
                       loader] * len(unique_urls), [download_folder] * len(unique_urls)), total=len(unique_urls)))

    # Keeping only MP4 files and deleting others
    for filename in os.listdir(download_folder):
        if not filename.endswith(".mp4"):
            file_path = os.path.join(download_folder, filename)
            os.remove(file_path)

    print("All videos downloaded and filtered successfully")
    input("Press Enter to exit...")

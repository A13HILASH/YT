from pytube import YouTube
from tqdm import tqdm
import requests
import threading
import sys
import os
import re

def main(): 
    while True:
        # Example URL: https://www.youtube.com/watch?v=VIDEO_ID
        video_url = input("Enter the YouTube video URL: ")
        validation = validate_and_download(video_url)
        if validation:
            download_video(video_url)
        else:
            print("Invalid YouTube video URL.")
        confirmation = input("Would you like to download another video? (y/n): ").lower()
        if confirmation == 'n':
            print("Exit Success.")
            break

def validate_and_download(video_url):
    # Regex to match various YouTube video URL formats
    match = re.search(r'(?:youtu\.be\/|v=)([0-9A-Za-z_-]+)', video_url)
    if not match:
        return False
    else: return True

def show_available_resolutions(video):
    print("Available Resolutions:")
    for i, stream in enumerate(video.streams, start=1):
        print(f"{i}. {stream.resolution} - {stream.mime_type} - Size: {format_size(stream.filesize)}")

def format_size(size_in_bytes):
    # Convert bytes to human-readable format (KB, MB, GB, etc.)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    invalid_chars = r'<>:"/\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def download_video(video_url, output_path="."):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Check if the video is age-restricted
        if yt.age_restricted:
            print("Age restricted video. Cannot be downloaded.")
            return

        # Show available resolutions with size
        show_available_resolutions(yt)

        # Ask the user to choose a resolution by number
        while True:
            try:
                choice = int(input("Enter the number corresponding to the resolution you want to download: "))
                if 1 <= choice <= len(yt.streams):
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get the chosen stream
        ys = yt.streams[choice - 1]

        # Sanitize the filename
        sanitized_filename = sanitize_filename(yt.title)

        # Confirm the download with size information
        print(f"\nYou have chosen to download: {yt.title}")
        print(f"Resolution: {ys.resolution}")
        print(f"Size: {format_size(ys.filesize)}")

        confirmation = input("Do you want to proceed with the download? (y/n): ").lower()

        if confirmation == 'y':
            # Create the full path to the Downloads directory
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{sanitized_filename}.{ys.subtype}")

            # Check if file already exists and get the resume bytes
            resume_bytes = 0
            if os.path.exists(downloads_path):
                resume_bytes = os.path.getsize(downloads_path)

            # Download the video with tqdm for progress
            print("\nDownloading... Press 'Ctrl + C' to cancel.")
            response = requests.get(ys.url, stream=True, headers={'Range': f'bytes={resume_bytes}-'})
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024

            # Function to update tqdm progress bar
            def update_progress_bar(bar, data):
                bar.update(len(data))

            # Create a thread for updating progress
            progress_thread = threading.Thread(target=lambda: sys.stdout.flush())
            progress_thread.start()

            with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as bar:
                try:
                    with open(downloads_path, 'ab') as f:  # Open in append binary mode
                        for data in response.iter_content(block_size):
                            update_progress_bar(bar, data)
                            f.write(data)
                except KeyboardInterrupt:
                    print("\nDownload canceled.")
                    sys.exit()
                except requests.exceptions.RequestException as e:
                    print(f"\nError: {str(e)}. Download failed.")
                    sys.exit()
            progress_thread.join()
            print(f"\nDownload complete! Saved to: {downloads_path}")
        else:
            print("Download canceled.")

    except Exception as e:
        print(f"Error: {str(e)}")
        

if __name__ == "__main__":
    main()


        





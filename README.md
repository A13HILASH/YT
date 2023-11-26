# YouTube Video Downloader

#### Video Demo: <https://dai.ly/k3mIc8XDkLoR59zGKej>

#### Description:
YouTube Video Downloader is a command-line tool designed to simplify the process of downloading YouTube videos. Built in Python, this project leverages the Pytube library to interact with the YouTube API and facilitate seamless video downloads. The main goal of the project is to provide a user-friendly interface for downloading videos, allowing users to choose their preferred resolution and ensuring a hassle-free experience.

## Features:
- **URL Validation:** The program uses regular expressions to validate YouTube video URLs, ensuring that users input a valid link before proceeding with the download.

- **Resolution Selection:** Users have the flexibility to choose the resolution of the video they want to download. The program displays all available resolutions, along with corresponding file sizes, enabling users to make informed decisions.

- **Informative Output:** Throughout the download process, the program provides informative output, including progress bars and size information, keeping users updated on the status of their downloads.

- **Age-Restricted Video Support:** The program checks for age-restricted videos and informs users when a video cannot be downloaded due to age restrictions.

## Design Choices

### 1. Command-Line Interface (CLI)
The decision to implement YouTube Video Downloader as a command-line tool was driven by a focus on simplicity and accessibility. A CLI allows users to interact with the tool directly from their terminal or command prompt, providing a familiar and lightweight user interface. This decision aims to cater to a diverse audience with varying levels of technical expertise. Users, regardless of their platform, can easily run the tool without the need for a graphical user interface, making it versatile and widely accessible.

### 2. Regular Expressions for URL Validation
Utilizing regular expressions for URL validation plays a crucial role in enhancing the robustness of the tool. YouTube video URLs come in various formats, and ensuring their validity is paramount to preventing common errors. The use of regular expressions allows the tool to accurately verify that the provided URL conforms to expected patterns, reducing the likelihood of invalid inputs. This design choice contributes to the overall reliability of the YouTube Video Downloader, ensuring a seamless user experience by catching potential issues early in the process.

By combining a command-line interface with robust URL validation, the design choices aim to create an intuitive and dependable tool for downloading YouTube videos. Users can initiate downloads with confidence, knowing that the tool is designed with simplicity, accessibility, and error prevention in mind.


## Project Structure

### `project.py`
The main script serving as the entry point for the YouTube Video Downloader. It contains the `main()` function for user interaction and additional functions for URL validation, resolution selection, and the download process.

### `test_project.py`
Comprehensive test suite for the project using the `pytest` framework. Each test function corresponds to a specific function in `project.py`.

### `requirements.txt`
List of pip-installable libraries necessary for running the project, including dependencies like `pytube`, `tqdm`, `requests`, and `pytest` with specific version numbers.


## How to Use:
1. Run the `project.py` script.
2. Enter a valid YouTube video URL when prompted.
3. Choose the desired video resolution from the provided list.
4. Confirm the download and wait for the process to complete.

## Requirements:
- Python 3.x
- Pytube library (15.0.0)
- tqdm library (4.66.1)
- requests library (2.31.0)
- pytest library (7.4.3)





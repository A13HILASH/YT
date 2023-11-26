import pytest
from unittest.mock import patch, MagicMock
from project import sanitize_filename, format_size, download_video, show_available_resolutions, validate_and_download


#-------------------------------------------
def test_validate_url():

    # Test case 1: Valid url
    result = validate_and_download("https://www.youtube.com/watch?v=VIDEO_ID")
    assert result == True

    # Test case 2: Invalid url
    result = validate_and_download("hdg91738")
    assert result == False
#-------------------------------------------

#-------------------------------------------
def test_sanitize_filename():
    # Test case 1: No invalid characters
    result = sanitize_filename("music_video")
    assert result == "music_video"

    # Test case 2: Replace invalid characters with underscores
    result = sanitize_filename(':*/mus<i>c?v|deo\"')
    assert result == "___mus_i_c_v_deo_"

    # Test case 3: Empty filename
    result = sanitize_filename("")
    assert result == ""
#-------------------------------------------


#------------------------------------------
@pytest.mark.parametrize("size_in_bytes, expected_output", [
    (1023, "1023.00 B"),
    (2048, "2.00 KB"),
    (1572864, "1.50 MB"),
    (1073741824, "1.00 GB")
])

def test_format_size(size_in_bytes, expected_output):
    result = format_size(size_in_bytes)
    assert result == expected_output
    
#-------------------------------------------


#-------------------------------------------
@pytest.mark.parametrize("streams, expected_output", [
    (
        [MagicMock(resolution="720p", mime_type="video/mp4", filesize=1024),
         MagicMock(resolution="480p", mime_type="video/mp4", filesize=512)],
        'Available Resolutions:\n1. 720p - video/mp4 - Size: 1.00 KB\n2. 480p - video/mp4 - Size: 512.00 B\n'
    )
])
def test_show_available_resolutions(capsys, streams, expected_output):
    # Mock the video object
    video = MagicMock()
    video.streams = streams

    # Call the function and capture printed output
    show_available_resolutions(video)
    captured = capsys.readouterr()

    # Check if the expected output is present
    assert captured.out =='Available Resolutions:\n1. 720p - video/mp4 - Size: 1.00 KB\n2. 480p - video/mp4 - Size: 512.00 B\n'
#-------------------------------------------


#-------------------------------------------
@pytest.mark.parametrize("video_url, user_input, expected_output", [
    ("https://www.youtube.com/watch?v=VIDEO_ID", '2\n', "Download canceled."),  # Simulate user input of '2' for the second choice
    
])
def test_download_video(capsys, monkeypatch, video_url, user_input, expected_output):
    # Mock the YouTube object
    yt_mock = MagicMock()
    yt_mock.age_restricted = False
    yt_mock.streams = [MagicMock(resolution="720p", mime_type="video/mp4", filesize=1024),
                      MagicMock(resolution="480p", mime_type="video/mp4", filesize=512)]

    # Monkeypatch the input function to return the predefined user input
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    # Use patch to mock the YouTube class
    with patch("project.YouTube", return_value=yt_mock):
        # Call the function and capture printed output
        download_video(video_url)

        # Check if the expected output is present
        captured = capsys.readouterr()
        assert expected_output in captured.out
#-------------------------------------------

if __name__ == "__main__":
    pytest.main()
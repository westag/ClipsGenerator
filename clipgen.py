# Import the required libraries
import os
from pytube import YouTube

url = input('Enter the YouTube URL: ')

def VideoDownload():
    # Create a YouTube object
    yt = YouTube(url)
    # Get the video with the highest resolution
    video = yt.streams.get_highest_resolution()

    if video is not None:
        # Set the output file name
        output_name = "File1V.mp4"
        # Set the output directory
        output_dir = "DOWNLOADED VIDEO OUTPUT PATH HERE"
        # Create the output path by joining the output directory and file name
        output_path = os.path.join(output_dir, output_name)
        # Download the video
        video.download(output_dir, output_name)
        print("Video downloaded successfully to:", output_path)
    else:
        print("No video stream available for download.")

def AudioDownload():
    # Create a YouTube object
    yt = YouTube(url)
    # Get the audio stream
    audio_stream = yt.streams.get_audio_only()
    # Set the output file name
    output_name = "File1A.mp3"
    # Set the output directory
    output_dir = "DOWNLOADED AUDIO OUTPUT PATH HERE"
    # Create the output path by joining the output directory and file name
    output_path = os.path.join(output_dir, output_name)
    # Download the audio
    audio_stream.download(output_dir, output_name)
    print("Audio downloaded successfully to:", output_path)

def Combine():
    import subprocess
    # Set the paths to the audio and video files
    audio_path = "DOWNLOADED AUDIO INPUT PATH HERE"
    video_path = "DOWNLOADED VIDEO INPUT PATH HERE"
    # Set the output file path
    output_path = "COMBINED FILE OUPUT PATH HERE"
    # Use ffmpeg to combine the audio and video files
    subprocess.run(["ffmpeg", "-i", audio_path, "-i", video_path, "-c", "copy", output_path])
    print("Audio and video combined successfully!")


def Spiltter():
    # Replace with the path to the YouTube video file
    input_path = 'COMBINED FILE INPUT PATH HERE'
    # Replace with the path to the folder where you want to save the video clips
    output_path = 'CLIPS OUTPUT HERE'
    # Split the video into 30 second clips
    os.system(f"ffmpeg -i {input_path} -c copy -map 0 -segment_time 30 -f segment {output_path}/%d.mp4")

    # Convert the clips to 1080x1920 resolution
    for video in os.listdir(output_path):
        if video.endswith(".mp4"):
            os.system(f"ffmpeg -i {output_path}/{video} -vf scale=1080:1920 {output_path}/1080x1920_{video}")
            os.remove(f"{output_path}/{video}")
    print('Video Successfully Spilt!')

VideoDownload()
AudioDownload()
Combine()
Spiltter()

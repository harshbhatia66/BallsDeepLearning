import os
import sys
import time
import youtube_dl
import yt_dlp

def download_recent_videos(channel_url, num_videos, folder):
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'min_duration': 120,
        'max_duration': 1200,
        # Only go through the first 5 pages of videos
        'playlistend': 1000
    }
    
    yt = yt_dlp.YoutubeDL(ydl_opts)
    print(yt)
    print("done")
    videos = yt.extract_info(channel_url, download=False, ie_key='YoutubeTab')
    video_count = 0
    # Download into the folder
    os.chdir(folder)
    
    for video in videos['entries']:
        if video_count >= num_videos:
            break
        
        if video.get('duration') is not None and video.get('duration') > 20*60:
            continue
        
        video_url = video['webpage_url']
        try:
            yt.download([video_url])
            print(f"Downloaded {video['title']} as mp3.")
        except:
            print(f"Error downloading {video['title']}.")
        
        video_count += 1
        time.sleep(1)

channel_url = "https://www.youtube.com/channel/UCq6VFHwMzcMXbuKyG7SQYIg/videos"
num_videos = 1000
folder = r'C:\Users\Harsh\Documents\gap\gapvoice\audio_preprocessing\mp3'
download_recent_videos(channel_url, num_videos, folder)

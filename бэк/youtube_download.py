import yt_dlp
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_video(url, output_file_name):
    ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                'outtmpl': output_file_name
                }
    URLS = [url]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)



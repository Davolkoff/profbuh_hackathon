from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re

def get_chapters(url):
    # Ключ API YouTube Data API
    api_key = 'AIzaSyAoOhWLQA0RYIqTQtV6OSO14TqSB5_nKtw'

    # ID видео на YouTube
    video_id = url[32::]

    # Создание YouTube Data API клиента
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        # Запрос на получение списка глав видео
        response = youtube.videos().list(
            part='snippet',
            id=video_id,
        ).execute()

        if response['items']:
            description = response['items'][0]['snippet']['description']


    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
    pattern = r"(\d+:\d+)\s\|\s(.+)\s"
    timestamps = re.findall(pattern, description)

    return timestamps
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Set up the API client
api_key = ""
youtube = build('youtube', 'v3', developerKey=api_key)


def searchyoutube_videos(search_query, max_results=100):

    now=datetime.utcnow()
    three_months_ago = now -timedelta(days=90)


    search_response = youtube.search().list(
    q=search_query,
    part='snippet',
    type='video',
    maxResults=max_results,
    publishedAfter=three_months_ago.isoformat() + 'Z'  # Convert datetime to ISO 8601 format
).execute()

    videos = search_response['items']


    video_urls =[]

    for video in videos:
        video_id = video['id']['videoId']
        video_urls.append(f"https://youtube.com/watch?v={video_id}")

    return video_urls

from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Set up the API client
api_key = "AIzaSyAQX50f262Fllww3hdXkfEw6e7X99-PyrE"
youtube = build('youtube', 'v3', developerKey=api_key)


def search_videos(search_query, max_results=100):

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



def search_youtube_bis():
 
    # Paramètres de recherche
    params = {
        'part': 'snippet',
        'type': 'channel',
        'maxResults': 50,  # Nombre maximal de résultats par page
        'order': 'subscriberCount',  # Tri par nombre d'abonnés
        'q': 'francais',  # Mot-clé pour rechercher les chaînes en français
        'relevanceLanguage': 'fr',  # Langue de pertinence (français)
        'maxResults': 50,  # Nombre maximal de résultats par page
    }
    
    # Effectuer la requête de recherche
    search_response = youtube.search().list(**params).execute()
    
    # Liste pour stocker les résultats
    results = []
    
    # Parcourir les résultats de recherche
    for item in search_response['items']:
        channel_id = item['id']['channelId']
        channel_response = youtube.channels().list(part='snippet,brandingSettings', id=channel_id).execute()
        channel_title = channel_response['items'][0]['snippet']['title']
        channel_description = channel_response['items'][0]['snippet']['description']
        about_text = channel_response['items'][0]['brandingSettings']['channel']['description']
        email = channel_response['items'][0]['brandingSettings']['channel'].get('email', 'N/A')
        
        result = {
            'title': channel_title,
            'description': channel_description,
            'about': about_text,
            'email': email
        }
        
        results.append(result)
    
    return results


print(results)
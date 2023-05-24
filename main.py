import logging
from api.youtube_api import search_videos
from processing.ask import ask_youtube

# Configuration du module de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Recherche de vidéos YouTube
keyword = "python tutorial"
videos = search_videos(keyword)

# Traitement du transcript
for video in videos:
    transcript = search_videos(video)
    questions = ask_youtube("what is this about",transcript)

    logging.info(f"Video: {video}")
    logging.info(f"Questions: {questions}")

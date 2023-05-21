import os
os.environ["OPENAI_API_KEY"]=""
from langchain.document_loaders import YoutubeLoader
from langchain.indexes import VectorstoreIndexCreator

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=zizonToFXDs", add_video_info=False)
index = VectorstoreIndexCreator().from_loaders([loader])
query= " What the author of the video says about agents and tools?"
result = index.query(query)

def ask_youtube(query,urls):

    answers=[]
    for url in urls:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
        index = VectorstoreIndexCreator().from_loaders([loader])
        query = query
        result = index.query(query)
        answers.append(result)

    return answers


langchain_videos=["https://youtube.com/watch?v=fCh7PKR5WqU","https://youtube.com/watch?v=4p1Fojur8Zw"]



import openai
import os
os.environ["OPENAI_API_KEY"]="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"
from langchain.document_loaders import YoutubeLoader
from langchain.indexes import VectorstoreIndexCreator


def ask_youtube(query,urls):

    answers=[]
    for url in urls:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
        index = VectorstoreIndexCreator().from_loaders([loader])
        query = query
        result = index.query(query)
        answers.append(result)

    return answers





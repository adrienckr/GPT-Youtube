from langchain.text_splitter import CharacterTextSplitter
llm = OpenAI(temperature=0)
loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=U29z_IOLfFM", add_video_info=False)
docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)
chain = load_summarize_chain(llm, chain_type="map_reduce")
print(chain.run(split_docs))

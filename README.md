# YouTube Video Learning Tool

This project aims to create a tool that allows users to learn 10 times faster from YouTube videos. The tool consists of three files: `fetch-youtube.py`, `summarize-youtube.py`, and `query-youtube.py`. Each file serves a specific purpose in the overall workflow of the tool.

## Requirements
To run this project, you need to have the following requirements installed:

- Python 3.x
- Google API Client Library
- langchain

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:



## File Descriptions

### 1. `fetch-youtube.py`
This file is responsible for fetching YouTube video information using the YouTube Data API. It retrieves metadata such as video title, description, duration, and other relevant details. The fetched information is stored in a structured format for further processing.

To use this file:
1. Obtain a YouTube Data API key from the Google Developers Console.
2. Open `fetch-youtube.py` in a text editor and replace the placeholder `YOUR_API_KEY` with your actual API key.
3. Run the script by executing the following command:



The script will prompt you to enter the YouTube video URL or video ID. It will then retrieve the video information and save it to a file for later use.

### 2. `summarize-youtube.py`
This file utilizes the langchain library to summarize YouTube videos. It takes the video information fetched by `fetch-youtube.py` and generates concise summaries that capture the key points of each video. The summaries can be helpful in quickly understanding the video content without watching the entire video.

To use this file:
1. Make sure you have a file containing the fetched YouTube video information, e.g., `video_info.json`.
2. Open `summarize-youtube.py` in a text editor and specify the path to the video information file by modifying the `VIDEO_INFO_FILE` variable.
3. Run the script by executing the following command:



The script will generate summaries for each video and display them on the console.

### 3. `query-youtube.py`
This file allows users to query YouTube videos using the langchain library. It takes a user's query as input and searches for relevant YouTube videos based on the query content. The results can be useful for finding specific videos related to a particular topic of interest.

To use this file:
1. Run the script by executing the following command:



The script will prompt you to enter your query. After providing the query, it will search for relevant YouTube videos and display the results.

## Usage Recommendations
1. Use `fetch-youtube.py` to gather information about specific YouTube videos of interest.
2. Employ `summarize-youtube.py` to quickly understand the content of the fetched videos without watching them entirely.
3. Utilize `query-youtube.py` to find YouTube videos related to specific topics or queries.

## Important Notes
- Ensure you have a stable internet connection for accessing the YouTube Data API and retrieving video information.
- The YouTube Data API key provided should be kept confidential and not shared publicly.
- This tool serves as a supplementary aid for learning from YouTube videos and does not replace the actual video content.

## License
This project is licensed under the [MIT License](LICENSE).

Please refer to the individual files for additional comments and usage instructions. If you encounter any issues or have suggestions for improvement,

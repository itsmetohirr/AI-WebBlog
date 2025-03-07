import os
import re

import dotenv
from openai import OpenAI
from supadata import Supadata
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import TextFormatter

dotenv.load_dotenv()

# def get_transcript(url):
#     """
#     Extracts the video ID from a YouTube URL and fetches its transcript.
#     Args:
#         url (str): The YouTube video URL.
#     Returns:
#         str: The formatted transcript as plain text.
#     """
#     pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/|.*[?&]v=)|youtu\.be\/)([\w-]{11})'
#     video_id = re.search(pattern, url).group(1)

#     transcript = YouTubeTranscriptApi.get_transcript(video_id)
#     formatter = TextFormatter()
#     text = formatter.format_transcript(transcript)

#     return text


def get_transcript(url):
    api_key = os.getenv('SUPADATA_API_KEY')
    supadata = Supadata(api_key=api_key)

    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/|.*[?&]v=)|youtu\.be\/)([\w-]{11})'
    video_id = re.search(pattern, url).group(1)

    text_transcript = supadata.youtube.transcript(
        video_id=video_id,
        text=True
    )

    return text_transcript.content


def summarize_transcript(text):
    """
    Generates a creative HTML blog content based on a given transcript using OpenAI.
    Args:
        text (str): The transcript text.
    Returns:
        str: The generated HTML content for the blog.
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "developer", "content": "You are a blog post writer."},
            {
                "role": "user",
                "content": (
                    "Based on the following transcript from a YouTube video, create a highly creative html content that summarizes the video. Use emojis, highlights, headings, different fonts and more to keep it interesting, divide the content into paragaphs for better readablity."
                    f"Transcript:\n\n{text}\n\n"
                ),
            },
        ],
        max_tokens=1000,
    )
    
    content = response.choices[0].message.content
    return content


# video_url = 'https://youtu.be/-qjE8JkIVoQ?si=bRiQdFq5q36yWuPk'

# transcript = get_transcript(video_url)
# print(transcript)
# print(summarize_transcript(transcript))

import os
import re

import dotenv
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

dotenv.load_dotenv()

def get_transcript(url):
    """
    Extracts the video ID from a YouTube URL and fetches its transcript.
    Args:
        url (str): The YouTube video URL.
    Returns:
        str: The formatted transcript as plain text.
    """
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/|.*[?&]v=)|youtu\.be\/)([\w-]{11})'
    video_id = re.search(pattern, url).group(1)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    text = formatter.format_transcript(transcript)

    return text


def blog_from_transcript(text):
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
                    "Based on the following transcript from a YouTube video, "
                    "write HTML content for a creative blog article. Divide the blog into proper paragraphs, "
                    "use emojis, and keep the language human. Use highly creative HTML content to make the blog engaging: "
                    "use highlighting, headings, colors, and more. If possible, add some relevant pictures from the internet.\n\n"
                    f"Transcript:\n\n{text}\n\n"
                ),
            },
        ],
        max_tokens=1000,
    )
    
    content = response.choices[0].message.content
    return content

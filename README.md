# SumAI

SumAI is a powerful tool that takes a YouTube video link and generates a concise and accurate summary of its content using advanced natural language processing techniques. Whether you're looking to save time or quickly grasp the key points of a video, SumAI has got you covered!

## 🚀 Features

- 🎥 Accepts any YouTube video link.
- 🧠 Uses OpenAI to analyze and summarize the video content.
- 📄 Provides a text-based summary that is easy to read and understand.
- ⏱️ Saves time by condensing long videos into digestible summaries.

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sumai.git
cd sumai
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variables:

```bash
cp .env.example .env
```

Add your API keys and configuration details to the `.env` file.

## 🚦 Usage

To initialize Django project run:

```bash
./manage.py runserver
```

You will get a summarized output of the video's content.

## 🧰 Technologies Used

- **Python**: Core programming language
- **SupaData API**: To fetch video data
- **OpenAI API (gpt-4o)**: To generate summaries
- **Django**: (Optional) For building a web interface

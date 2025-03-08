# SumAI

SumAI — bu YouTube video havolasini qabul qilib, uning mazmunini qisqa va aniq tarzda umumlashtirib beruvchi qulay vosita. Agar vaqtingizni tejashni yoki videoning asosiy fikrlarini tezda anglab olishni xohlasangiz, SumAI sizga yordam beradi!

## 🚀 Xususiyatlar

- 🎥 Har qanday YouTube video havolasini qabul qiladi.
- 🧠 Video mazmunini tahlil qilish va umumlashtirish uchun rivojlangan AI texnologiyasidan foydalanadi.
- 📄 O'qish va tushunish oson bo'lgan matnli xulosa taqdim etadi.
- ⏱️ Uzoq videolarni qisqa mazmunlarga aylantirib, vaqtingizni tejaydi.

## 🛠️ O'rnatish

1. Repozitoriyani klonlash:

```bash
git clone https://github.com/yourusername/sumai.git
cd sumai
```

2. Kerakli kutubxonalarni o'rnatish:

```bash
pip install -r requirements.txt
```

3. Muhit o'zgaruvchilarini sozlash:

```bash
cp .env.example .env
```

API kalitlari va sozlash ma'lumotlarini `.env` fayliga qo'shing.

## 🚦 Foydalanish

Djangoni ishga tushirish uchun:

```bash
python app.py --url "https://www.youtube.com/watch?v=example"
```

Natijada videoning qisqa mazmuni olinadi.

## 🧰 Ishlatilgan texnologiyalar

- **Python**: Asosiy dasturlash tili
- **Google API**: Video ma'lumotlarini olish uchun
- **SupaData API**: Video transkript olish uchun
- **OpenAI GPT (yoki boshqa NLP modeli)**: Xulosa yaratish uchun
- **Django**: Veb interfeys yaratish uchun


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
- **Django**: For building a web interface

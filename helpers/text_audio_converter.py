import json
from gtts import gTTS


def converter():
    with open("files/news_data.csv", "r") as file:
        news_data = file.read()

    news_data = json.loads(news_data)
    text = ""

    for i, j in news_data.items():
        text += "Next Next Next " + str(i)

    speech = gTTS(text=text, lang="en", slow=False)
    with open('files/test.mp3', 'wb') as f:
        speech.write_to_fp(f)
    print("Audio created successfully")


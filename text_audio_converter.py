import json
from gtts import gTTS


def converter():
    with open("news_data.json", "r") as file:
        news_data = file.read()

    news_data = json.loads(news_data)
    text = ""

    for i, j in news_data.items():
        text += "Next Next Next " + str(i)

    speech = gTTS(text=text, lang="en", slow=False)
    with open('test.mp3', 'wb') as f:
        speech.write_to_fp(f)
    print("Audio created successfully")


converter()

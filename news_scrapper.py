import requests
from bs4 import BeautifulSoup
import json


def news_scraper():
    response = requests.get("https://pulse.zerodha.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    rev_div = soup.findAll("li", attrs={"class", "box item"})
    data = {}

    for i in range(len(rev_div)):
        data[rev_div[i].find("a").text] = rev_div[i].find("div").text

    with open('news_data.json', 'a') as file:
        json_string = json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=2)
        file.write(json_string)
    file.close()


news_scraper()

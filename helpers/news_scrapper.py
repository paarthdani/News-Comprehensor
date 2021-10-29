import requests
from bs4 import BeautifulSoup
import csv


def news_scraper():
    response = requests.get("https://pulse.zerodha.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    rev_div = soup.findAll("li", attrs={"class", "box item"})
    return add_data(rev_div)


def add_data(rev_div):
    news_data_list = []
    result_list = []
    with open('files/news_data.csv', mode='r', encoding='utf-8', newline='') as news_data:
        news_reader = csv.reader(news_data, delimiter=',')
        for row in news_reader:
            news_data_list.append(row[0])

    with open('files/news_data.csv', mode='a', encoding='utf-8', newline='') as news_data:
        news_writer = csv.writer(news_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(rev_div)):
            if rev_div[i].find("a").get('data-id') not in news_data_list:
                result_list.append([rev_div[i].find("a").get('data-id'),
                                    rev_div[i].find("a").text,
                                    rev_div[i].find("a").get('href')])
                news_writer.writerow([rev_div[i].find("a").get('data-id'),
                                      rev_div[i].find("a").text,
                                      rev_div[i].find("a").get('href')])
        return result_list


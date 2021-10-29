from helpers import news_scrapper
from helpers import text_audio_converter
from helpers import alert_generator

if __name__ == '__main__':
    updated_news_list = news_scrapper.news_scraper()
    alert_generator.alert_generator(updated_news_list)
    # text_audio_converter.converter()


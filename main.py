from helpers import news_scrapper
from helpers import alert_generator
from flask import Flask
import logging

app = Flask(__name__)

logger = logging.getLogger()
logging.basicConfig(filename="system.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a',
                    level=logging.DEBUG)


@app.route('/')
def news_comprehensor():
    updated_news_list = news_scrapper.news_scraper()
    logger.info("updated news list is " + str(updated_news_list))
    alert_generator.alert_generator(updated_news_list)
    return {"200": "Success"}


if __name__ == "__main__":
    app.run()
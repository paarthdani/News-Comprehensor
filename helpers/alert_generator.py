import requests


def alert_generator(data_list):
    telegram_url = 'https://api.telegram.org/botxx/sendMessage?chat_id=-xx&text='
    count = 0
    for i in data_list:
        post_message = telegram_url + i[1] + ".\n" + i[2]
        requests.post(post_message)
        if count == 2:
            break
        count += 1

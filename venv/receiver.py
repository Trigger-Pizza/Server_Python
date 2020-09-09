import requests
import time
from datetime import datetime

def pretty_print(message):
    dt = datetime.fromtimestamp(message['timestamp'])
    dr = dt.strftime('%Y/%m/%d %H:%M:%S')
    dr = dr + '  ' + message['name']
    print(dr)
    if (message['text'] == 'Hitler'):
        message['text'] = 'Bad guy'
        print(' ' + message['text'])
        print(' ')
        print('Товарищ майор' + '  ' + dt.strftime('%Y/%m/%d %H:%M:%S'))
        print('Пройдемте в отделение товарищ!')
        print(' ')
    elif (message['text'] == 'Fuck'):
        message['text'] = 'Bad word'
        print(' ' + message['text'])
        print(' ')
        print('Товарищ майор' + '  ' + dt.strftime('%Y/%m/%d %H:%M:%S'))
        print('Не сквернословь!')
        print(' ')
    else:
        print(' ' + message['text'])
    print(' ')

url = 'http://127.0.0.1:5000/messages'

after_id = -1

while True:
    response = requests.get(url, params={'after_id': after_id})
    messages = response.json()['messages']
    for message in messages:
        pretty_print(message)
        after_id = message['id']
    time.sleep(1)



from flask import Flask, request, jsonify
from flask_sslify import SSLify
from requests.api import delete
from secret_data import SecretData
from validation import validation
from create_image import create_image
import requests
import json

app = Flask(__name__)
data = SecretData ()
token = data.token
domen = data.domen

URL = 'https://api.telegram.org/bot' + token + '/'
number = 0

def write_json(data, filename = 'answer.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent = 2, ensure_ascii = False)

def send_message(chat_id, text = "неверный текст"):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

def send_photo(chat_id, path):
    url = URL + 'sendPhoto'
    files = {'photo': open('/path/to/img.jpg', 'rb')}
    answer = {'chat_id': chat_id}
    r = requests.post(url, files = files, data = answer)
    return r.json()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        valid_data = validation(message)
        if (valid_data[0] == False):
            send_message(chat_id, text = valid_data[1])
        else:
            number+=1
            path = create_image(quantity = valid_data[1]['quantity'],
                        price = valid_data[1]['price'], 
                        artical = valid_data[1]['artical'], 
                        title = valid_data[1]['title'],
                        name = number)
            write_json(send_photo(chat_id, path))
            number-=1
        return jsonify(r)
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    app.run()
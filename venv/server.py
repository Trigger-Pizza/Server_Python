from flask import Flask, request
import time

app = Flask(__name__)
name = input('Введите имя пользователя: ')
timestamp = time.asctime()

db = []
requested_count = 0

@app.route("/")
def hello():
    return "Hello my lord!: <a href='/status'>My status</a>"

@app.route("/status")
def status():
    return {"status":True, 'name': name, 'time': timestamp}

@app.route("/send", methods=['POST'])
def send():
    data = request.json
    db.append({
        'id':len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': time.time()
    })
    return {'ok': True}



@app.route("/messages")
def messages():
   if 'after_id' in request.args:
      after_id = int(request.args['after_id']) + 1
   else:
       after_id = 0
   return {'messages':db[after_id:]}

app.run()
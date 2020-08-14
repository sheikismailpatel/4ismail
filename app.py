from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def init():
    return 'enter the following link : "https://basic-ismail.herokuapp.com/0" where 0 is id for first student'

@app.route('/<int:id>')
def index(id):
    
    json = {
        "name": "rajiv",
        "marks": {
                    "Maths": 18,
                    "English": 21,
                    "Science": 45
        },
        "rollNumber": "KV2017-5A2"
    }
    json2 = {
        "name": "abhishek",
                "marks": {
                    "Maths": 43,
                    "English": 30,
                    "Science": 37
                },
                "rollNumber": "KV2017-5A1"

    }
    json3 = { 
        "name": "zoya",
                "marks": {
                    "Maths": 42,
                    "English": 31,
                    "Science": 50
                },
                "rollNumber": "KV2017-5A3"
    }
    data = [json, json2, json3]
    if id < 3:
        return data[id]
    else:
        return 'Please choose 0 or 1 or 2'


if __name__ == '__main__':
    app.run()
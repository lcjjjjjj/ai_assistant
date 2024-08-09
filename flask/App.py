from flask import Flask, request, jsonify
from flask_cors import CORS
from Textsum import text_rewrite

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route("/")
def hello():
    return "<p>hello,world</p>"

@app.route('/upload', methods=['POST','GET'])
def recv_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('test.py')
    return 'file recived'

@app.route('/textsum', methods=['POST'])
def recv_text():
    data = request.json
    result = text_rewrite(data['text'])
    # print(result)
    response = {
        'msg': result
    }
    return jsonify(response)
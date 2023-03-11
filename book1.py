# initialization
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.route('/foo', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def foo():
    return request.json['inputVar']

if __name__ == '__main__':
   app.run()

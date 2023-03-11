'''from flask_cors import CORS, cross_origin
# code using with request argument.
from flask import Flask, request,jsonify
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
cors = CORS(app, resources={r"/Get": {"origins": "http://localhost:3000/"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['supports_credentials']=True
#app.config['CORS_HEADERS'] = 'Content-Type
CORS(app)'''

from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/GET": {"origins": "http://localhost:8080"}})
@app.route('/Get',methods=['GET'])
def query_example():


    language = request.args.get('filter')
    
    t = {"data":[{"AppointmentId":3,"Text":"Isssnstall New Router in Dev Room","Description":None,"StartDate":"2021-04-26T21:30:00.000Z","EndDate":"2021-04-26T22:30:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None}]}
#,{"AppointmentId":4,"Text":"Approve Personal Computer Upgrade Plan","Description":None,"StartDate":"2021-04-27T17:00:00.000Z","EndDate":"2021-04-27T18:00:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None},{"AppointmentId":5,"Text":"Final Budget Review","Description":None,"StartDate":"2021-04-27T19:00:00.000Z","EndDate":"2021-04-27T20:35:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None},{"AppointmentId":6,"Text":"New Brochures","Description":None,"StartDate":"2021-04-27T21:30:00.000Z","EndDate":"2021-04-27T22:45:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None},{"AppointmentId":7,"Text":"Install New Database","Description":None,"StartDate":"2021-04-28T16:45:00.000Z","EndDate":"2021-04-28T18:15:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None},{"AppointmentId":8,"Text":"Approve New Online Marketing Strategy","Description":None,"StartDate":"2021-04-28T19:00:00.000Z","EndDate":"2021-04-28T21:00:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None}]}
    #return {"data":[{"AppointmentId":3,"Text":"Install New Router in Dev Room","Description":'sdfdsfds',"StartDate":"2021-04-26T21:30:00.000Z","EndDate":"2021-04-26T22:30:00.000Z","AllDay":'false',"RecurrenceRule":''null'',"RecurrenceException":''null''},{"AppointmentId":4,"Text":"Approve Personal Computer Upgrade Plan","Description":''null'',"StartDate":"2021-04-27T17:00:00.000Z","EndDate":"2021-04-27T18:00:00.000Z","AllDay":'false',"RecurrenceRule":''null'',"RecurrenceException":'''null'''},{"AppointmentId":5,"Text":"Final Budget Review","Description":''null'',"StartDate":"2021-04-27T19:00:00.000Z","EndDate":"2021-04-27T20:35:00.000Z","AllDay":false,"RecurrenceRule":''null'',"RecurrenceException":''null''},{"AppointmentId":6,"Text":"New Brochures","Description":''null'',"StartDate":"2021-04-27T21:30:00.000Z","EndDate":"2021-04-27T22:45:00.000Z","AllDay":false,"RecurrenceRule":'null',"RecurrenceException":'null'},{"AppointmentId":7,"Text":"Install New Database","Description":'null',"StartDate":"2021-04-28T16:45:00.000Z","EndDate":"2021-04-28T18:15:00.000Z","AllDay":false,"RecurrenceRule":'null',"RecurrenceException":'null'},{"AppointmentId":8,"Text":"Approve New Online Marketing Strategy","Description":'null',"StartDate":"2021-04-28T19:00:00.000Z","EndDate":"2021-04-28T21:00:00.000Z","AllDay":false,"RecurrenceRule":'null',"RecurrenceException":'null'}]}
    response = jsonify(t)
    #response = jsonify({'message': 'Hello, world!'})
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:8080/')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response
@app.route('/Post',methods=['POST'])
def query_example1():
    language = request.args.get('values')
    return []
   
@app.route('/Delete')
def query_example2():
    language = request.args.get('key')
    return []
@app.route('/Put')
def query_example3():
    language = request.args.get('key')
    language = request.args.get('values')
    return []

  
  
'''@app.route('/Get')
def query_example():
    language = request.args.get('filter')

  
@app.route('/Get')
def query_example():
    language = request.args.get('filter')'''
    
  
if __name__ == '__main__':
    app.run(debug=True, port=8080)

from flask import Flask,render_template,redirect,jsonify,request,session
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

lst = []
# app.secret_key = 'abcd'
@app.route('/proc',methods=['POST'])
def appendText():
    if ('stop' not in request.json['query']):
        txt = request.json['query']
        lst.append(str(txt))
    else:
        f = open('./meetingStore/store.txt','w')
        if lst:
            f.write('.\n'.join(lst))
            # print (session['txt'])
            
            # session.pop('txt',None)

        lst.clear()
    return jsonify([{'reply':'stored'}])

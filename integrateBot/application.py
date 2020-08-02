from flask import render_template, redirect, Flask, request
import requests
import json
from bitbucket.client import Client

app = Flask(__name__)
@app.route('/')
def mainPage():
    return 'hello world'

# @app.route('/tokentransfer',methods=['GET'])
# def storeToken():
#     tokenStr = str(request.args.get('code'))
#     return tokenStr

#     # return render_template('submit.html')

# # @app.route('/printtoken',methods=['GET'])
# # def printToken():

@app.route('/comm/<userText>')
def process(userText):
    userChat = json.dumps({"sender": "Jamal","message": str(userText)})
    resp = requests.post("http://localhost:5005/webhooks/rest/webhook",data=userChat,
                     headers={'Content-type':'application/json','Accept':'text/plain'})
    if (resp.status_code == 200):
        returnList = []
        for i in resp.json():
            returnList.append(i['text'])
        
        return (', '.join(returnList))
    else:
        return (resp.text)


if __name__ == '__main__':
	app.run(debug=True)

# def getCode(repo,branch='master',durationVal,user=None):
#     if (user):
        

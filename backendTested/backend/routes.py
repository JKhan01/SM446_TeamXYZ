import json, requests, tempfile
from wsgi import app, token_storage
from flask import session, current_app, request, redirect, jsonify
from bson.objectid import ObjectId
from functools import wraps
from datetime import datetime
from flask_cors import cross_origin
# from botocore.exceptions import ClientError
# from CeleryApp.celery import app as celeryapp

def check_session(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'id' in session:
            exists = bool(token_storage.exists(session['id']))
            if not exists:
                return json.dumps({'status': 440, 'msg': 'session timed out'})
        else:
            session['id'] = str(ObjectId())
            token_storage.hset(session['id'], mapping={'login': 'true'})
            print(session['id'])
        return f(*args, *kwargs)
    return wrapper

#To do
def store_chat(chat):
    pass

#To do   
# def store_meeting(s3_bucket, key):
#     #(
#     #    s3_bucket: String(s3 bucket name)
#     #    key: String(filename in bukcet)
#     # ) -> String(ObjectId for document)
#     return str(ObjectId())

#chat
@app.route('/chat', methods=['POST'])
@check_session
def chat():
    query = request.json['query']
    userChat = json.dumps({"sender": "Jamal","message": str(query)})
    resp = requests.post("http://localhost:5005/webhooks/rest/webhook",data=userChat,
                    headers={'Content-type':'application/json','Accept':'text/plain'})
    if (resp.status_code ==200):
        returnList = []
        for i in resp.json():
            try:
                var = json.loads(i['text'])
                returnList.append({'reply':var['reply']})
            except Exception:
                returnList.append({'reply':i['text']})
        return jsonify(returnList)
    else:
        return jsonify([{'reply':'Connection Problem to the response processing sever'}])
    
# @app.route('/meeting', methods=['POST'])
# @check_session
# def meeting():
#     token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])
#     jwt = token_storage.hmget(session['id'], 'google')[0]
#     if jwt is None:
#         return json.dumps({'status': 401, 'type': 'google', 'msg': 'google account not connected'})
#     else:
#         try:
#             tf = tempfile.TemporaryFile()
#             tf.write(request.data)
#             tf.seek(0)
#             filename = str(ObjectId())
#             s3.upload_fileobj(tf, current_app.config['S3_BUCKET'], filename)
#             document_id = store_meeting(current_app.config['S3_BUCKET'], filename)
#             celeryapp.send_task('tasks.transcribe', args=[document_id])
#             tf.close()
#         except ClientError as e:
#             #To do: log error
#             return json.dumps({'status': 503, 'msg':'unable to store audio'})
#     return json.dumps({'status': 200})

#AUTH
@app.route('/auth/bitbucketGen', methods=['GET'])
@check_session
def auth_bitbucket():
    return redirect(f'https://bitbucket.org/site/oauth2/authorize?client_id={current_app.config["PRODUCT_KEY_BITBUCKET"]}&response_type=code')



@app.route('/auth/bitbucket', methods=['GET'])
@check_session
def genTokenBitbucket():
    access_code = str(request.args.get('code'))
    response = requests.post('https://bitbucket.org/site/oauth2/access_token',data={'grant_type':'authorization_code','code': access_code},
              auth=(current_app.config["PRODUCT_KEY_BITBUCKET"],current_app.config["PRODUCT_SECRET_BITBUCKET"]))
    if response.status_code == 200:
        access_token = response.json()['access_token'] #token from bitbucket
        refreshToken = response.json()['refresh_token']
        token = json.dumps({'access': access_token, 'refresh': refreshToken})
        token_storage.hset(session['id'], mapping={'bitbucket': token})
        token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])
        return 'success'#redirect(current_app.config['FRONTEND_URL'])
    else:
       return 'Access Confirmation Failed' 
# @app.route('/auth/google', methods=['POST'])
# @check_session
# def auth_google():
#     token = '123' #token from google
#     token_storage.hset(session['id'], mapping={'google': token})
#     token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])

# @app.route('/auth/confluence', methods=['POST'])
# @check_session
# def auth_confluence():
#     token = '123' #token from confluence
#     token_storage.hset(session['id'], mapping={'confluence': token})
#     token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])

# @app.route('/auth/jira', methods=['POST'])
# @check_session
# def auth_jira():
#     token = '123' #token from jira
#     token_storage.hset(session['id'], mapping={'jira': token})
#     token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])

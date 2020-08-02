import json, requests, tempfile
from wsgi import db, token_storage, app, s3
from flask import session, current_app, request, redirect
from bson.objectid import ObjectId
from functools import wraps
from datetime import datetime
from botocore.exceptions import ClientError
from CeleryApp.celery import app as celeryapp



def check_session(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'id' in session:
            exists = bool(token_storage.exists(session['id']))
            if not exists:
                return json.dumps({'status': 440, 'msg': 'session timed out'})
        else:
            session['id'] = str(ObjectId())
            return f(*args, *kwargs)
    return wrapper

#To do
def store_chat(chat):
    pass

#To do   
def store_meeting(s3_bucket, key):
    #(
    #    s3_bucket: String(s3 bucket name)
    #    key: String(filename in bukcet)
    # ) -> String(ObjectId for document)
    return str(ObjectId())

#chat
@app.route('/chat', methods=['POST'])
@check_session
def chat(query):
        token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])
        content = {'sender': session['id'], 'message': str(query)}
        response = requests.post(current_app.config['RASA_ACTION_SERVER_URL'], json=content)
        # To do: process response from bot and return to frontend
        return 

@app.route('/meeting', methods=['POST'])
@check_session
def meeting():
    token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])
    jwt = token_storage.hmget(session['id'], 'google')[0]
    if jwt is None:
        return json.dumps({'status': 401, 'type': 'google', 'msg': 'google account not connected'})
    else:
        try:
            tf = tempfile.TemporaryFile()
            tf.write(request.data)
            tf.seek(0)
            filename = str(ObjectId())
            s3.upload_fileobj(tf, current_app.config['S3_BUCKET'], filename)
            document_id = store_meeting(current_app.config['S3_BUCKET'], filename)
            celeryapp.send_task('tasks.transcribe', args=[document_id])
            tf.close()
        except ClientError as e:
            #To do: log error
            return json.dumps({'status': 503, 'msg':'unable to store audio'})
    return json.dumps({'status': 200})

#AUTH
@app.route('/auth/bitbuket', methods=['POST'])
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
        token = response.json()['access_token'] #token from bitbucket
        refreshToken = response.json()['refresh_token']
        token_storage.hset(session['id'], mapping={'bitbucket': token})
        token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])
        return redirect(current_app.config['FRONTEND_URL'])
    else:
        return 'Access Confirmation Failed' 
@app.route('/auth/google', methods=['POST'])
@check_session
def auth_google():
    token = '123' #token from google
    token_storage.hset(session['id'], mapping={'google': token})
    token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])

@app.route('/auth/confluence', methods=['POST'])
@check_session
def auth_confluence():
    token = '123' #token from confluence
    token_storage.hset(session['id'], mapping={'confluence': token})
    token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])

@app.route('/auth/jira', methods=['POST'])
@check_session
def auth_jira():
    token = '123' #token from jira
    token_storage.hset(session['id'], mapping={'jira': token})
    token_storage.expire(session['id'], current_app.config['SESSION_TIMEOUT'])

from .celery import app, token_store

#write any functions which are to be performed aync or periodically here
# mails etc

@app.task
def send_mail():
    #to do
    pass
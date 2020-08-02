# Sending an Email

from g4 import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import mimetypes
import json
from email import encoders
 

#  Sending an email

def SendMail():
    # Body of the email
    emailMsg = input(print("Enter the body of the email :"))

    mimeMessage = MIMEMultipart()

    # Recipient's mail address
    print("To send to multiple recipients, separate the mail ids by a semi-colon (Format is 'sample1@gmail.com; sample2@gmail.com'\n")
    print("Enter the recipient's email address (Format is 'sample@gmail.com') : ")
    mimeMessage['to'] = input()

    # Subject of the mail
    mimeMessage['subject'] = input(print("Enter the subject of the email : "))

    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)
    return (json.dumps(message))       # returns the message variable or sent email in JSON format
    #return (print(json.dumps(message)))      # this could be used to directly print the JSON file in front end


# Sending an email with attachments

def SendMailWithAttachments():
    # Body of the email
    emailMsg = input(print("Enter the body of the email :"))

    mimeMessage = MIMEMultipart()

    # Recipient's mail address
    # To send to multiple recipients, separate the mail ids by a semi-colon
    print("To send to multiple recipients, separate the mail ids by a semi-colon\n")
    print("Enter the recipient's email address (Format is 'sample@gmail.com') : ")
    mimeMessage['to'] = input()

    # Subject of the mail
    mimeMessage['subject'] = input(print("Enter the subject of the email : "))

    mimeMessage.attach(MIMEText(emailMsg, 'plain'))    
    
    number_of_attachments = int(input(print("Enter the number of attachments to be attached : ")))
    #i = 0
    for i in range(number_of_attachments) :
        file_dir = input(print("Enter the directory in which the file is stored : "))
        filename = input(print("Enter the name of the file (with extension): "))
        path = os.path.join(file_dir, filename)
        content_type, encoding = mimetypes.guess_type(path)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'

        main_type, sub_type = content_type.split('/', 1)

        # For a text file
        if main_type == 'text':
            fp = open(path, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()

        # For an image
        elif main_type == 'image':
            fp = open(path, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()

        # For an audio file
        elif main_type == 'audio':
            fp = open(path, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()

        # All the other types of files
        else:
            fp = open(path, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()

        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        encoders.encode_base64(msg)
        mimeMessage.attach(msg)

    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)
    return (json.dumps(message))       # returns the message variable or sent email in JSON format
    #return (print(json.dumps(message)))      # this could be used to directly print the JSON file in front end





CLIENT_SECRET_FILE = 'credentials2.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
 

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


# Code for testing

print("How do you want to send the email : \n" + "1. Without any attachment\n" + "2. With attachment/s\n")
option = int(input())

if option == 1 : 
    SendMail()

elif option == 2 :
    SendMailWithAttachments()
# Searching and retrieving emails in inbox

from g4 import Create_Service
import base64
import email
import json

CLIENT_SECRET_FILE = 'credentials2.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

user_id = "me"
# print("For retrieving emails from a specific user, give query as 'from: sample@gmail.com'\n" + "For retrieving emails through their labels, give query as 'label_name'")
# query = input(print("Enter your query : "))

#messages = ListMessagesMatchingQuery(service, user_id, query)

# prints every message from the user
#print(messages)

'''

if not messages:
    print("No messages found")
else:
    print("The latest message from the specified user or label is :")
    for message in messages[:1]:
        # For retrieving details about the email
        msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
        #print(msg['snippet'])
        msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
        final_msg = email.message_from_bytes(msg_str)
        #print(final_msg)

        # For getting the entire body of the mail
        m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
        body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
        print(body)


'''



class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)





def ListMailsMatchingQuery(service, user_id, query):
  
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except:
    print ('An error occurred')




def GetLatestMailFromUser():
    print("For retrieving emails from a specific user, give query as 'from: sample@gmail.com'")
    query = input(print("Enter your query : "))
    messages = ListMailsMatchingQuery(service, user_id, query)

    if not messages:
        print("No messages found")
    else:
        #print("The latest message from the specified user or label is :")
        for message in messages[:1]:
            
            print("What information do you need about the latest email : " + "\n 1. Entire Info\n 2. Body snippet\n 3. Subject\n 4. Entire Body")
            op = int(input())


            if op == 1 :
                # For retrieving details about the email
                # Getting the complete body of the email
                m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
                body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")

                
                # For retrieving details about the email
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                

                display = Object()
                display.From = final_msg["From"]
                display.To = final_msg["To"]
                display.Subject = final_msg["Subject"]
                display.body = body
                
                #print(final_msg)       # It prints the entire info about the email
                return (print(display.toJSON()))   # Returns display[] as a JSON file


            elif op == 2 :
                
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))   
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['snippet'])
                #return (print(json.dumps(final_msg['snippet'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['snippet']))       # returns the snippet of the mail in JSON format

            elif op == 3 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['Subject'])
                #return (print(json.dumps(final_msg['Subject'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['Subject']))       # returns the Subject of the mail in JSON format

            elif op == 4 :  
                # For getting the entire body of the mail 
                m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
                body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
                print(body)
                #return (print(json.dumps(body)))    # this could be used to directly print the JSON file in front end
                return (json.dumps(body))       # returns the snippet of the mail in JSON format

            else:
                print("Invalid Input")     




def GetLatestMailFromLabel():
    print("For retrieving emails through their labels, give query as 'label_name'")
    query = input(print("Enter your query : "))
    messages = ListMailsMatchingQuery(service, user_id, query)

    if not messages:
        print("No messages found")
    else:
        #print("The latest message from the specified user or label is :")
        for message in messages[:1]:
            
            print("What information do you need about the latest email : " + "\n 1. Entire Info\n 2. Body snippet\n 3. Subject\n 4. Entire Body\n 5. Sender\n 6. Receiver")
            op = int(input())


            if op == 1 :
                # Getting the complete body of the email
                m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
                body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")

                
                # For retrieving details about the email
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                

                display = Object()
                display.From = final_msg["From"]
                display.To = final_msg["To"]
                display.Subject = final_msg["Subject"]
                display.body = body
                
                #print(final_msg)       # It prints the entire info about the email
                return (print(display.toJSON()))   # Returns display[] as a JSON file

            elif op == 2 :
                
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))   
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['snippet'])
                #return (print(json.dumps(final_msg['snippet'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['snippet']))       # returns the snippet of the mail in JSON format       

            elif op == 3 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['Subject'])
                #return (print(json.dumps(final_msg['Subject'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['Subject']))       # returns the Subject of the mail in JSON format

            elif op == 4 :  
                # For getting the entire body of the mail 
                m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
                body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
                print(body)
                #return (print(json.dumps(body)))    # this could be used to directly print the JSON file in front end
                return (json.dumps(body))       # returns the snippet of the mail in JSON format

            elif op == 5 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['From'])
                #return (print(json.dumps(final_msg['From'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['From']))       # returns the Sender of the mail in JSON format

            elif op == 6 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['To'])
                #return (print(json.dumps(final_msg['To'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['To']))       # returns the Receiver of the mail in JSON format

            else:
                print("Invalid Input")



def LatestMailInInbox():
    
    #try:
    response = service.users().messages().list(userId=user_id,
                                            labelIds = "INBOX").execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId=user_id, labelIds = "INBOX",
                                        pageToken=page_token).execute()
        messages.extend(response['messages'])

    # except:
    #     print ("An error occurred")


    if not messages:
        print("No messages found")
    else:
        #print("The latest message in the inbox is :")
        for message in messages[:1]:
            
            print("What information do you need about the latest email : " + "\n 1. Entire Info\n 2. Body snippet\n 3. Subject\n 4. Entire Body\n 5. Sender\n 6. Receiver")
            op = int(input())


            if op == 1 :
                
                # Getting the complete body of the email
                m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
                body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")

                
                # For retrieving details about the email
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                

                display = Object()
                display.From = final_msg["From"]
                display.To = final_msg["To"]
                display.Subject = final_msg["Subject"]
                display.body = body
                
                #print(final_msg)       # It prints the entire info about the email
                return (print(display.toJSON()))   # Returns display[] as a JSON file

            elif op == 2 :
                
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))   
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['snippet'])
                
                #return (print(json.dumps(final_msg['snippet'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['snippet']))       # returns the snippet of the mail in JSON format       

            elif op == 3 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['Subject'])
                #return (print(json.dumps(final_msg['Subject'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['Subject']))       # returns the Subject of the mail in JSON format

            elif op == 4 :  
                # For getting the entire body of the mail 
                m = service.users().messages().get(userId = 'me', id = message['id'], format='full').execute()
                body = base64.urlsafe_b64decode(m.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
                print(body)
                #return (print(json.dumps(body)))    # this could be used to directly print the JSON file in front end
                return (json.dumps(body))       # returns the body of the mail in JSON format

            elif op == 5 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['From'])
                #return (print(json.dumps(final_msg['From'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['From']))       # returns the Sender of the mail in JSON format

            elif op == 6 :
                msg = service.users().messages().get(userId = 'me', id = message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                final_msg = email.message_from_bytes(msg_str)
                print(final_msg['To'])
                #return (print(json.dumps(final_msg['To'])))    # this could be used to directly print the JSON file in front end
                return (json.dumps(final_msg['To']))       # returns the Receiver of the mail in JSON format

            else:
                print("Invalid Input")





#GetLatestMailFromUser()

#GetLatestMailFromLabel()

#LatestMailInInbox()
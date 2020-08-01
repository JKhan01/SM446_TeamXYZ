import imaplib
import email
from email.header import decode_header
import webbrowser
import os
username = ""   
password = ""
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
status, messages = imap.select("INBOX")
result , data = imap.uid('search',None,"ALL")
dataList = data[0].split()
Flag=0;
#for i in range(1):
print("1.Recent Mail"+"\n\n"+"2.Search"+"\n\n" , end="")
print("Enter your Option : - " , end="")
op=int(input())
if op==2:
    print("\n"+"Enter the user you want to search : - ",end="")
    name=input()
    for item in dataList:
        res,msg = imap.uid('fetch',item,'(RFC822)')
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                from_ = msg.get("From")
                string1 = name in from_
                if string1 == True:
                    print("\n"+"Subject : -", subject)
                    print("\n"+"From : -", from_)            
                    print("\n"+"Body Text : - "+"\n")
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                print(body)
                            elif "attachment" in content_disposition:
                                filename = part.get_filename()  
                                if filename:
                                    if not os.path.isdir(subject):
                                        os.mkdir(subject)
                                    filepath = os.path.join(subject, filename)
                                    open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                        content_type = msg.get_content_type()
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            print(body)
                else:
                    Flag=1;
if Flag==1:
    print("No User found")
if op==1:
    for i in range(1):
        recent = dataList[-1] 
        res,msg = imap.uid('fetch',recent,'(RFC822)')
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                from_ = msg.get("From")
                print("Subject : -", subject)
                print("From : -", from_)            
                print("Body Text : - "+"\n")
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                             print(body)
                        elif "attachment" in content_disposition:
                            filename = part.get_filename()  
                            if filename:
                                if not os.path.isdir(subject):
                                    os.mkdir(subject)
                                filepath = os.path.join(subject, filename)
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)
imap.close()
imap.logout()
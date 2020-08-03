#import essential liabraries
import requests
from requests.auth import HTTPBasicAuth
import json
import pprint

# OAUTH auth = HTTPBasicAuth("rohitkadyash@gmail.com", "UpwcB7QfUzWFxgqlxJAOE06E")

username = "rohitkadyash@gmail.com" #accept from user
apitoken = "UpwcB7QfUzWFxgqlxJAOE06E" #accept from user 

auth = HTTPBasicAuth( username , apitoken)

# def create_issue_epic(ename,summary, description , ver_name , p_name ,a_name  ):
#     url = "https://roriosa.atlassian.net/rest/api/3/issue"
#     headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json"
#     }
    
#     #issue type id
#     type_id = 0
#     type_id = get_issue_type_id(p_name, "Epic")
    
#     #reporter id that is creater id 
    
#     rep_id = self_userid()
    
    
#     #assignee id
#     if a_name == "myself":
#         a_id = rep_id
#     else :
#         a_id = get_userid(a_name)   
    
#     #find project id from name 
    
#     pro_id = get_projectid(p_name)
    
#     #get_versionid of the version name entered and project id 
#     ver_id = get_versionid(pro_id ,ver_name )
    
#     payload = json.dumps( {
#      "update": {},
#      "fields": {
#          "customfield_10011" : ename ,  # this is the place where epic name is placed
#          "summary": summary, #summary
#          "issuetype": {
#              "id": type_id
#               },
#          "project": {
#              "id": pro_id   #project id
#           },
#        "description":  {
#          "type": "doc",
#          "version": 1,
#          "content": [
#             {
#               "type": "paragraph",
#               "content": [
#                 {
#                    "text": description,  #description
#                    "type": "text"
#                 }
#                ]
#             }
#           ]
#        },
#       "reporter": {
#           "id": rep_id # creaters id is found
#        },
#        "fixVersions": [
#          {
#           "id": ver_id #version id
#          }
#          ],
         
#        #"duedate": "2020-29-07" , # due date eg "y-m-d" in date format
    
#        "assignee": {
#          "id": a_id#this is user id
#        }
#      }
#     } )
    
    
#     response = requests.request(
#     "POST",
#     url,
#     data=payload,
#     headers=headers,
#     auth=auth
#     )

#     resp_data = json.loads(response.text)
#     id1 = resp_data['id']
#     key = resp_data['key']
#     self = resp_data['self']
#     str = f"Epic created with id:{id1} , key: {key} , self: {self} " 
    
#     data = {}
#     data['reply'] = [str]
    
#     return data
    
# import datetime

    
#create_issue_epic( "epic is name","this is summary" , "this is the description " , "version3" , "Resume screening" ,"Jamal")    
    
    
    
    
    
    

    
    
    

def self_userid():
    url = "https://roriosa.atlassian.net/rest/api/3/myself"
    headers = {
       "Accept": "application/json"
    }
   
    response = requests.request(
     "GET",
     url,
     headers=headers,
     auth=auth
    )
    
    datava = json.loads(response.text)
    acc_id = datava["accountId"] 
    return acc_id

def get_issue_type_id(pname, itype):
    url = "https://roriosa.atlassian.net/rest/api/3/issue/createmeta"
    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
        url,
        headers=headers,
        auth=auth
     )

    data = json.loads(response.text)
    for attrs in data["projects"]:
        if attrs["name"] == pname:
            #print(attrs["issuetypes"])
            for datavar in attrs["issuetypes"]:
                if datavar["name"] == itype:
                    p_ident = datavar["id"]
                    break
    return p_ident

#val = get_issue_type_id("Resume screening","Sub-task")
#print(val)

def get_projectid(p_name):
    url = "https://roriosa.atlassian.net/rest/api/3/project"


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )
    p_ident = 0
    datavar = json.loads(response.text)
    for attrs in datavar:
        if attrs['name'] == p_name:
            p_ident = attrs['id']
            break
    return p_ident


def get_versionid(pro_id,ver_name):
    a = "https://roriosa.atlassian.net/rest/api/3/project/"
    b = "/versions"
    c = str(pro_id)
    xy = a+c
    url = xy+b
    headers = {
          "Accept": "application/json"
    }
    response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
    )

    data = json.loads(response.text)
    for attrs in data:
        if attrs['name'] == ver_name:
            v_ident = attrs['id']
            break
    return v_ident

def create_issue_bug(summary , description , ver_name , p_name , epic_summary , a_name): #ename is key of epic
    url = "https://roriosa.atlassian.net/rest/api/3/issue"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    
    #issue type id
    type_id = 0
    type_id = get_issue_type_id(p_name, "Bug")
    
    #epic key
    ekey = get_key(epic_summary)
    
    
    #reporter id that is creater id 
    rep_id = self_userid()

    #assignee id
    if a_name == "myself":
        a_id = rep_id
    else :
        a_id = get_userid(a_name)   
    
    
    #find project id from name 
    
    pro_id = get_projectid(p_name)
    
    #get_versionid of the version name entered and project id 
    ver_id = get_versionid(pro_id ,ver_name )
    
    payload = json.dumps( {
     "update": {},
     "fields": {
         "customfield_10014": ekey ,
         "summary": summary, #summary
         "issuetype": {
             "id": type_id
              },
         "project": {
             "id": pro_id   #project id
          },
       "description":  {
         "type": "doc",
         "version": 1,
         "content": [
            {
              "type": "paragraph",
              "content": [
                {
                   "text": description,  #description
                   "type": "text"
                }
               ]
            }
          ]
       },
      "reporter": {
          "id": rep_id # creaters id is found
       },
       "fixVersions": [
         {
          "id": ver_id #version id
         }
         ],
         
       #"duedate": "2020-29-07" , # due date eg "y-m-d" in date format
    
       "assignee": {
         "id": a_id#this is user id
       }
     }
    } )
    
    
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    resp_data = json.loads(response.text)
    id1 = resp_data['id']
    key = resp_data['key']
    self = resp_data['self']
    str1 = f"Bug created with id:{id1} , key: {key} , self: {self} " 
    
    data = {}
    data['reply'] = [str]
    
    return data
    
    
#create_issue_bug("syntactical error", "solve it description" , "version1" , "Resume screening" ,"this is summary" , "myself")



def get_key(isummary):
    iid = get_issue_id(isummary)

    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    a = str(iid)
   
    url = url+a


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    data = json.loads(response.text)
    if (isummary == (data["fields"]["summary"])):
        key = data["key"]
    
    return key
       


def create_issue_story(summary, description , ver_name , p_name ,  epic_summary , a_name): #ename is key of epic
    url = "https://roriosa.atlassian.net/rest/api/3/issue"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    
    #issue type id
    type_id = 0
    type_id = get_issue_type_id(p_name, "Story")
    
    #epic key
    ekey = get_key(epic_summary)
    #reporter id that is creater id 
    rep_id = self_userid()

    #assignee id
    if a_name == "myself":
        a_id = rep_id
    else :
        a_id = get_userid(a_name)   
    
    
    #find project id from name 
    
    pro_id = get_projectid(p_name)
    
    #get_versionid of the version name entered and project id 
    ver_id = get_versionid(pro_id ,ver_name )
    
    payload = json.dumps( {
     "update": {},
     "fields": {
         "customfield_10014": ekey ,
         "summary": summary, #summary
         "issuetype": {
             "id": type_id
              },
         "project": {
             "id": pro_id   #project id
          },
       "description":  {
         "type": "doc",
         "version": 1,
         "content": [
            {
              "type": "paragraph",
              "content": [
                {
                   "text": description,  #description
                   "type": "text"
                }
               ]
            }
          ]
       },
      "reporter": {
          "id": rep_id # creaters id is found
       },
       "fixVersions": [
         {
          "id": ver_id #version id
         }
         ],
         
       #"duedate": "2020-29-07" , # due date eg "y-m-d" in date format
    
       "assignee": {
         "id": a_id#this is user id
       }
     }
    } )
    
    
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    resp_data = json.loads(response.text)
    id1 = resp_data['id']
    key = resp_data['key']
    self = resp_data['self']
    str1 = f"Story created with id:{id1} , key: {key} , self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data
    
    
#create_issue_story("add to mongo db", "hello description" , "version1" , "Resume screening" ,"this is summary" , "myself")


def create_issue_task(summary , description , ver_name , p_name ,  epic_summary , a_name): #ename is key of epic
    url = "https://roriosa.atlassian.net/rest/api/3/issue"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    
    #issue type id
    type_id = 0
    type_id = get_issue_type_id(p_name, "Task")
    
    #epic key
    ekey = get_key(epic_summary)
    
    
    #reporter id that is creater id 
    rep_id = self_userid()

    #assignee id
    if a_name == "myself":
        a_id = rep_id
    else :
        a_id = get_userid(a_name)   
    
    
    #find project id from name 
    
    pro_id = get_projectid(p_name)
    
    #get_versionid of the version name entered and project id 
    ver_id = get_versionid(pro_id ,ver_name )
    
    payload = json.dumps( {
     "update": {},
     "fields": {
         "customfield_10014": ekey ,
         "summary": summary, #summary
         "issuetype": {
             "id": type_id
              },
         "project": {
             "id": pro_id   #project id
          },
       "description":  {
         "type": "doc",
         "version": 1,
         "content": [
            {
              "type": "paragraph",
              "content": [
                {
                   "text": description,  #description
                   "type": "text"
                }
               ]
            }
          ]
       },
      "reporter": {
          "id": rep_id # creaters id is found
       },
       "fixVersions": [
         {
          "id": ver_id #version id
         }
         ],
         
       #"duedate": "2020-29-07" , # due date eg "y-m-d" in date format
    
       "assignee": {
         "id": a_id#this is user id
       }
     }
    } )
    
    
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )
    
    resp_data = json.loads(response.text)
    id1 = resp_data['id']
    key = resp_data['key']
    self = resp_data['self']
    
    str1 = f"task created with id:{id1} , key: {key} , self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data
    
    
    
#create_issue_task("this is task", "solve it description" , "version1" , "Resume screening" ,"this is summary","jamal")
def create_issue_subtask(summary , description , ver_name , p_name ,  task_summary,a_name): #ename is key of epic
    url = "https://roriosa.atlassian.net/rest/api/3/issue"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    
    #issue type id
    
    type_id = get_issue_type_id(p_name, "Sub-task")
    #print(type_id)
    
    #task key
    tkey = get_key(task_summary)
    
    #task id
    tid = get_issue_id(task_summary)
    
    #print(tkey)
    
    
    #reporter id that is creater id 
    rep_id = self_userid()

    #assignee id
    if a_name == "myself":
        a_id = rep_id
    else :
        a_id = get_userid(a_name)   
    
    
    #find project id from name 
    
    pro_id = get_projectid(p_name)
    
    #get_versionid of the version name entered and project id 
    ver_id = get_versionid(pro_id ,ver_name )
    
    payload = json.dumps( {
     "update": {},
     "fields": {
         
         "summary": summary, #summary
         "issuetype": {
             "id": type_id
              },
         "project": {
             "id": pro_id   #project id
          },
       "description":  {
         "type": "doc",
         "version": 1,
         "content": [
            {
              "type": "paragraph",
              "content": [
                {
                   "text": description,  #description
                   "type": "text"
                }
               ]
            }
          ]
       },
         
       "parent":{
             "key": tkey ,
             "id" : tid
         },  
      "reporter": {
          "id": rep_id # creaters id is found
       },
       "fixVersions": [
         {
          "id": ver_id #version id
         }
         ],
         
       #"duedate": "2020-29-07" , # due date eg "y-m-d" in date format
    
       "assignee": {
         "id": a_id#this is user id
       }
     }
    } )
    
    
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    resp_data = json.loads(response.text)
    id1 = resp_data['id']
    key = resp_data['key']
    self = resp_data['self']
    str1 = f"Sub task created with id:{id1} , key: {key} , self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data
    
    
    
#create_issue_subtask("this is subtask", "solve it description" , "version1" , "Resume screening" ,"this is task" , "jamal")

def get_userid(u_name) :
    url = "https://roriosa.atlassian.net/rest/api/3/groupuserpicker"


    headers = {
       "Accept": "application/json"
    }

    query = {
       'query': username
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       params=query,
       auth=auth
    )

    data = json.loads(response.text)
    
    return data['users']['users'][0]['accountId']
    
#get_userid("jamal")

def get_all_project_name():
    
    url = "https://roriosa.atlassian.net/rest/api/3/project"


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )
    
      
    data = []
    datavar = json.loads(response.text)
    for attrs in datavar:
        name = attrs['name']
        str1 = f"project - {name}"
        data.append(str1)
    x = ", ".join(data)
    
    ret_data = {}
    ret_data['reply'] = x
    
    return ret_data
        
#get_all_project_name()


def create_version(rel_date , start_date , name , description ,pro_name , released):
    url = "https://roriosa.atlassian.net/rest/api/3/version"
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
      }
    
    pro_id = get_projectid(pro_name)
    
    if released == "false" or released == "False" :
        payload = json.dumps( {
          "archived": False,
          "releaseDate": rel_date,
          "startDate" : start_date,  # eg i/p "2020-07-24" 
          "name": name, #enter name of version
          "description": description, #enter description 
          "projectId": pro_id , #add the id to link version to a project
          "released": False #if the version is already released boolean value
          } )
    if released == "true" or released =="True" :
        payload = json.dumps( {
          "archived": False,
          "releaseDate": rel_date,
          "startDate" : start_date,  # eg i/p "2020-07-24" 
          "name": name, #enter name of version
          "description": description, #enter description 
          "projectId": pro_id , #add the id to link version to a project
          "released": True #if the version is already released boolean value
          } )
        
    response = requests.request(
     "POST",
     url,
     data=payload,
     headers=headers,
     auth=auth
    ) 
    
    resp_data = json.loads(response.text)
    id1 = resp_data['id']
    name = resp_data['name']
    start = resp_data['startDate']
    rel = resp_data['releaseDate']
    self = resp_data['self']
    str1 = f"Version created with id:{id1} , name: {name} , startDate: {start} ,release date: {rel} ,self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data



def create_project(template, typekey , name , key , description,lead_name):
    url = "https://roriosa.atlassian.net/rest/api/3/project"
    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }
    
    if template == "content management" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-content-management"
    if template == "document approval" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval"
    if template == "lead tracking" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking"
    if template == "process control" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control"    
    if template == "procurement" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-procurement"
    if template == "project management" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-project-management"    
    
    if template == "recruitment" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment"  
        
    if template == "task tracking" and typekey == "business" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking"  
        
    if template == "it" and typekey == "service desk" :
        template_key = "com.atlassian.servicedesk:simplified-it-service-desk"
        typekey = "service_desk"
    if template == "internal" and typekey == "service desk" :
        template_key = "com.atlassian.servicedesk:simplified-internal-service-desk"
        typekey = "service_desk"
    if template == "external" and typekey == "service desk" :
        template_key = "com.atlassian.servicedesk:simplified-external-service-desk"
        typekey = "service_desk"
    if template == "kanban" and typekey == "software" :
        template_key = "com.pyxis.greenhopper.jira:gh-simplified-agility-kanban" 
    
    if template == "scrum" and typekey == "software" :
        template_key = "com.pyxis.greenhopper.jira:gh-simplified-agility-scrum" 
    
    if template == "task tracking" and typekey == "software" :
        template_key = "com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking" 
    
    
    
    
    #when self assign the leader then assignee type field is kept unassigned and if other user then assigneetype
    #is kept PROJECT_LEAD
    if lead_name == "myself" or lead_name == "Myself" :
        leadid = self_userid()
        assigneetype = "UNASSIGNED"
    else :
        leadid = get_userid("lead_name")
        assigneetype = "PROJECT_LEAD"

    payload = json.dumps( {
         #"notificationScheme": 10021,
         "description": description,
         #"lead": "Rohit Kadam",
         "leadAccountId": leadid,  #selfid
         "url": "http://roriosa.atlassian.com",
         "projectTemplateKey": template_key , #take template from user
         #"avatarId": 10200,
         #"issueSecurityScheme": 10001,
         "name": name ,
         #"permissionScheme": 10011,
         "assigneeType": assigneetype, # two types of i/p -  PROJECT_LEAD , UNASSIGNED
         "projectTypeKey": typekey , #take from user whether business or service_desk or software
         "key": key,
         #"categoryId": 10120
        } )

    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
      )

    resp_data = json.loads(response.text)
    id1 = resp_data['id']
    key = resp_data['key']
    self = resp_data['self']
    
    str1 = f"Project created with id:{id1} , key: {key} , self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data
    
#create_project("scrum" , "software" , "demo name of jamal project" , "JMP" , "demo description")

def create_group(gname):
    url = "https://roriosa.atlassian.net/rest/api/3/group"
    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "name": gname
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )

    resp_data = json.loads(response.text)
    name = resp_data['name']
    self = resp_data['self']
    str1 = f"Group created with name:{name} , self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data
    
#create_group("demo group")


def add_user_to_group(gname , uname):


    url = "https://roriosa.atlassian.net/rest/api/3/group/user"

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    query = {
       'groupname': gname
    }
    
    if uname == "myself" or "Myself" :
        uid = self_userid()
    else :
        uid = get_userid(uname)
    
    payload = json.dumps( {
      "accountId": uid
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       params=query,
       auth=auth
    )

    resp_data = json.loads(response.text)
    
    name = resp_data['name']
    self = resp_data['self']
    str1 = f"user addedd to group name:{name} , self: {self} " 
    
    data = {}
    data['reply'] = [str1]
    
    return data
   
#add_usertogroup("demo group" , "myself")

def get_users_in_group(gname):

    url = "https://roriosa.atlassian.net/rest/api/3/group/member"


    headers = {
       "Accept": "application/json"
    }

    query = {
       'groupname': gname
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       params=query,
       auth=auth
    )
    
    data = []
    datavar = json.loads(response.text)
    for attrs in datavar.values():
        id = attrs['accountId']
        name = get_username(id)
        data.append(name)
        
    x = ", ".join(data)
    
    
    ret_data = {}
    ret_data['reply'] = x
    
    return ret_data

    
#get_users_in_group("demo group")

def get_username(u_id):
    url = "https://roriosa.atlassian.net/rest/api/3/groupuserpicker"


    headers = {
       "Accept": "application/json"
    }

    query = {
       'query': u_id
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       params=query,
       auth=auth
    )

    data = json.loads(response.text)
    
    return data['users']['users'][0]['displayName']
    

def get_issues_in_project(pname):
    url = "https://roriosa.atlassian.net/rest/api/3/search/"

    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )
    
    ret_data = {}
    ret_list = []
    data = json.loads(response.text)
    #pprint.pprint(data)
    for element in data["issues"] :
        if pname == element["fields"]["project"]["name"] :
            iname = element["fields"]["summary"]
            ikey = element["key"]
            str1 = f"issue name : {iname} and key: {ikey}"
            ret_list.append(str1)
    x = ", ".join(ret_list)
    
    ret_data['reply'] = x
    
    
    return ret_data
#pprint.pprint(get_issues_in_project("Resume screening"))


def get_issue(isummary):
    iid = get_issue_id(isummary)

    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    a = str(iid)
   
    url = url+a


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    #pprint.pprint(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    data = json.loads(response.text)
    description = data['fields']['description']['content'][0]['content'][0]['text']
    issue_type = data['fields']['issuetype']['name']
    status = data['fields']['status']['name']
    summary = data['fields']['summary']
    
    str1 = f"issue name: {summary}, description: {description}, issue type: {issue_type}, status: {status} "
    
    ret_data = {}
    ret_data['reply'] = str1
    
    return ret_data
    
    
#get_issue("this is task")

def get_issue_id(name):
    url = "https://roriosa.atlassian.net/rest/api/3/search/"

    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    resp = json.loads(response.text)
    #pprint.pprint(resp["issues"])
    
    for data in resp["issues"]:
        if data["fields"]["summary"] == name :
            iid = data["id"]
        
    return iid

#get_issue_id("hello people")

def get_status_of_issue(isummary):
    iid = get_issue_id(isummary)

    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    a = str(iid)
   
    url = url+a


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    #pprint.pprint(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    data = json.loads(response.text)
    stat = data["fields"]["status"]["name"]
    str1 = f"status is : {stat}"
    
    ret_data = {}
    ret_data['reply'] = str1
    
    return ret_data
    
    

#get_status_of_issue("learn space")

def get_issue_version(isummary):  # and also release date
    iid = get_issue_id(isummary)

    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    a = str(iid)
   
    url = url+a


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    #pprint.pprint(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    data = json.loads(response.text)
    date = data["fields"]["fixVersions"][0]["releaseDate"]
    name = data["fields"]["fixVersions"][0]["name"]
    str1 = f"issue belongs to version: {name} and will release on date: {date} "
    
    ret_data = {}
    ret_data['reply'] = str1
    
    return ret_data
    
    
#get_issue_version("this is task")   


def add_comment(visible_to_role , comment , i_summary ):
    
    iid = get_issue_id(i_summary)
    iid = str(iid)
    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/comment"
    url = url + iid
    url= url+b
    
    
    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "visibility": {
        "type": "role",
        "value": visible_to_role#"Administrators"
      },
      "body": {
        "type": "doc",
        "version": 1,
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "text": comment,
                "type": "text"
              }
            ]
          }
        ]
      }
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    data = json.loads(response.text)
    text = data['body']['content'][0]['content'][0]['text']
    self = data['self']
    visible = data['visibility']['value']
    str1 = f"comment added : {text} ,visible to : {visible}, self:{self} "
    ret_data = {}
    ret_data['reply'] = str1
    
    return ret_data

    
#add_comment("Administrators" , "watched youtube vedieo" , "hello people" )

def delete_comment(i_summary,comment):
    iid = get_issue_id(i_summary)
    cid = get_comments_id_in_issue(i_summary , comment )
    iid = str(iid)
    cid = str(cid)
    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/comment/"
    url = url +iid
    url = url +b
    url = url +cid
    

    response = requests.request(
       "DELETE",
       url,
       auth=auth
    )

    if response.text == "":
        str1 = f"comment {comment} is deleted from issue {i_summary}"
    else:
        str1 = "there is some mistake"
        
    ret_data = {}
    ret_data['reply'] = str1
    return ret_data


#delete_comment("hello people" , "watched youtube vedieo")


def get_comments_id_in_issue(isummary , com):  #com
    a = get_key(isummary)
    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/comment"
    url = url + a
    url = url + b


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    data = json.loads(response.text)
    for element in data["comments"] :
        if com == element["body"]["content"][0]["content"][0]["text"] :
            com_id = element["id"]
    return com_id 

#get_comments_id_in_issue("hello people" , "watched youtube vedieo")


def get_comments_in_issue(isummary):
    a = get_key(isummary)
    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/comment"
    url = url + a
    url = url + b


    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    ret_list = []
    ret_data = {}
    data = json.loads(response.text)
    for element in data["comments"] :
        comment = element["body"]["content"][0]["content"][0]["text"]
        id1 = element["id"]
        str1 = f"comment : {comment} , id: {id1}"
        ret_list.append(str1)
    
    x = ", ".join(ret_list)
    
    ret_data['reply'] = x
    return ret_data
    
#get_comments_in_issue("hello people")


def add_worklog(i_summary , comment,week,day,hour,minute,visible_role):
    iid = get_issue_id(i_summary)
    x = str(iid)
    a = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/worklog"
    c = a+x
    url = c+b
    
    time = str(week) + "w "
    time = time+str(day)
    time = time + "d "
    time = time + str(hour)
    time = time + "h "
    time = time + str(minute)
    time = time + "m"

    aid = self_userid()
    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "timeSpent": time,  #format 0w 1d 2h 30m
      "author" :{
          'accountId': aid
      },
      "visibility": {
        "type": "role",
        "value": visible_role
      },
      "comment": {
        "type": "doc",
        "version": 1,
        "content": [
          {
            "type": "paragraph",
            "content": [
              {
                "text": comment,
                "type": "text"
              }
            ]
          }
        ]
      },
      "started": "2020-07-27T07:01:40.217+0000"
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    data = json.loads(response.text)
    comment = data['comment']['content'][0]['content'][0]['text']
    self = data['self']
    time = data['timeSpent']
    str1 = f"worklog added with comment: {comment}, time spent: {time} and self:{self}"
    
    ret_data = {}
    ret_data['reply'] = str1
    
    return ret_data
    
    
#add_worklog("hello people","watch hotstar","0","0","3","15","Administrators")

def get_worklog_in_issue(i_summary): #prints worklog name and 
 
    iid = get_issue_id(i_summary)
    iid = str(iid)
    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/worklog"
    url = url + iid
    url = url + b

    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )
    ret_list = []
    data = json.loads(response.text)
    for element in data["worklogs"] :
        comment = element["comment"]["content"][0]["content"][0]["text"]
        time = element["timeSpent"]
        str1 = f"worklog : {element} , time spent: {time}"
        ret_list.append(str1)
    x = ", ".join(ret_list)
    
    ret_data = {}
    ret_data['reply'] = x
    return ret_data
    
    
#get_worklog_in_issue("hello people")

def get_worklog_id(i_summary , wname ):
    iid = get_issue_id(i_summary)
    iid = str(iid)
    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/worklog"
    url = url + iid
    url = url + b

    headers = {
       "Accept": "application/json"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=auth
    )

    data = json.loads(response.text)
    for element in data["worklogs"] :
        
        if element["comment"]["content"][0]["content"][0]["text"] == wname :
            wid = element["id"]
        
    return wid 

#get_worklog_id("hello people" , "watched netflix" ) #this got deleted in bellow step

def delete_worklog(i_summary , wname ):
    iid = get_issue_id(i_summary)
    iid = str(iid)
    wid = get_worklog_id(i_summary,wname)
    wid = str(wid)

    url = "https://roriosa.atlassian.net/rest/api/3/issue/"
    b = "/worklog/"
    
    url = url + iid
    url = url +b
    url = url +wid

   
    response = requests.request(
       "DELETE",
       url,
       auth=auth
    )

    if response.text == "":
        str1 = f"worklog {wname} is deleted from issue {i_summary}"
    else:
        str1 = "there is some mistake"
        
    ret_data = {}
    ret_data['reply'] = str1
    return ret_data
    
#delete_worklog("hello people" , "watched netflix" )

























import json
import requests

class bitbucketActions():
    def __init__(self):
        self.baseUrl = 'https://api.bitbucket.org/2.0/'
        self.returnJson = {}
        self.viewUrl = 'https://bitbucket.org/'
        # self.access_token = ''
    ## getting list of repos
    def get_repos(self,owner_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name))
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            for i in out['values']:
                returnVar.append(i['slug'])    
            self.returnJson['reply'] = ', '.join(returnVar)
            self.returnJson['status'] = resp.status_code     
        else:
            self.returnJson['reply'] = resp.text
            self.returnJson['status'] = resp.status_code
        return self.returnJson
    ## getting the list of branches on a repo
    def get_branches(self,repo_name,owner_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/branches/')
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            for i in out['values']:
                returnVar.append(i['name'])
            self.returnJson['reply'] = ', '.join(returnVar)
            self.returnJson['status'] = resp.status_code    
        else:
            self.returnJson['reply'] = resp.text
            self.returnJson['status'] = resp.status_code
        return self.returnJson    
    ## getting the list of watchers on a repo
    def get_watchers(self,repo_name,owner_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/watchers/')
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            for i in out['values']:
                returnVar.append(i["display_name"])
            self.returnJson['reply'] = ', '.join(returnVar) 
            
        else:
            self.returnJson['reply'] = resp.text
        self.returnJson['status'] = resp.status_code
        return self.returnJson
    ## getting the latest commit info by a user
    def get_commit_by_user(self,repo_name,owner_name,user_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/commits')
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            for i in out['values']:
                if str(user_name).casefold() in i['message']:
                    returnVar.append('Commit was done by: '+str(i['author']['user']['display_name']))
                    returnVar.append('Commit Message: ' + str(i['message']))
                    returnVar.append('date: ' + str(i['date'][:20]).replace('T',' '))
                    returnVar.append('pagelink: ' + str(i['links']['html']['href']))
                    sCode = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/src/'+i['hash']+'/')
                    # ,headers={'Authorization':'Bearer '+self.access_token})
                    if sCode.status_code == 200:
                        lst = [j['links']['self']['href'] for j in sCode.json()['values']]
                        linkStr = ',\n '.join(lst)
                        returnVar.append('codeLinks: ' + linkStr)
                    break
            self.returnJson['reply'] = ', '.join(returnVar)
        else:
            
            self.returnJson['reply'] = resp.text
        self.returnJson['status'] = resp.status_code
        return self.returnJson
    
    ## get the commit based on a specific message
    def get_commit_by_msg(self,repo_name,owner_name,msg):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/commits')
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            for i in out['values']:
                if str(msg).casefold() in i['message']:
                    returnVar.append('Commit was done by: '+str(i['author']['user']['display_name']))
                    returnVar.append('Commit Message: ' + str(i['message']))
                    returnVar.append('date: ' + str(i['date'][:20]).replace('T',' '))
                    returnVar.append('pagelink: ' + str(i['links']['html']['href']))
                    sCode = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/src/'+i['hash']+'/')
                    # ,headers={'Authorization':'Bearer '+self.access_token})
                    if sCode.status_code == 200:
                        lst = [j['links']['self']['href'] for j in sCode.json()['values']]
                        linkStr = ',\n '.join(lst)
                        returnVar.append('codeLinks: ' + linkStr)
                    break
            self.returnJson['reply'] = ', '.join(returnVar)
        else:
            
            self.returnJson['reply'] = resp.text
        self.returnJson['status'] = resp.status_code
        return self.returnJson

    ## get the latest commit
    def get_commit_latest(self,repo_name,owner_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/commits')
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            i = out['values'][0]
            returnVar.append('Commit was done by: '+str(i['author']['user']['display_name']))
            returnVar.append('Commit Message: ' + str(i['message']))
            returnVar.append('date: ' + str(i['date'][:20]).replace('T',' '))
            returnVar.append('pagelink: ' + str(i['links']['html']['href']))
            sCode = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/src/'+i['hash']+'/')
            if sCode.status_code == 200:
                lst = [j['links']['self']['href'] for j in sCode.json()['values']]
                linkStr = ',\n '.join(lst)
                returnVar.append('codeLinks: ' + linkStr)
            
            self.returnJson['reply'] = returnVar
        else:
            
            self.returnJson['reply'] = ["Sorry Couldn't find anything"]
        return self.returnJson

    ## get the latest commit on a branch
    def get_commit_by_branch(self,repo_name,owner_name,branch_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/commits/'+str(branch_name))
        # ,headers={'Authorization':'Bearer '+self.access_token})
        if resp.status_code == 200:
            out = resp.json()
            returnVar = []
            i = out['values'][0]
            returnVar.append('Commit was done by: '+str(i['author']['user']['display_name']))
            returnVar.append('Commit Message: ' + str(i['message']))
            returnVar.append('date: ' + str(i['date'][:20]).replace('T',' '))
            returnVar.append('pagelink: ' + str(i['links']['html']['href']))
            sCode = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/src/'+i['hash']+'/')
            # ,headers={'Authorization':'Bearer '+self.access_token})
            if sCode.status_code == 200:
                lst = [j['links']['self']['href'] for j in sCode.json()['values']]
                linkStr = ',\n '.join(lst)
                returnVar.append('codeLinks: ' + linkStr)
            
            self.returnJson['reply'] = returnVar
        else:
            
            self.returnJson['reply'] = resp.text
        self.returnJson['status'] = resp.status_code
        return self.returnJson
    
    def get_commit_by_branch_user_name(self,repo_name,owner_name,branch_name,user_name):
        self.returnJson = {}
        resp = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/commits/'+str(branch_name))
        if resp.status_code == 200:
            out = resp.json()
            returnVar = {}
            returnVar = []
            for i in out['values']:
                if str(msg).casefold() in i['message']:
                    returnVar.append('Commit was done by: '+str(i['author']['user']['display_name']))
                    returnVar.append('Commit Message: ' + str(i['message']))
                    returnVar.append('date: ' + str(i['date'][:20]).replace('T',' '))
                    returnVar.append('pagelink: ' + str(i['links']['html']['href']))
                    sCode = requests.get(self.baseUrl+'repositories/'+str(owner_name)+'/'+str(repo_name)+'/src/'+i['hash']+'/')
                    if sCode.status_code == 200:
                        lst = [j['links']['self']['href'] for j in sCode.json()['values']]
                        linkStr = ',\n '.join(lst)
                        returnVar.append('codeLinks: ' + linkStr)
                    break
            self.returnJson['reply'] = returnVar
        else:
            
            self.returnJson['reply'] = ["Sorry Couldn't find anything"]
        return self.returnJson
    
    
    
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from modules.Bitbucket import bitbucketActions
from modules.ErrorSearch import searchStack
import json
from functions import *
from jira_package import *
from g5 import *
from g6 import *

obj = bitbucketActions()

class CommitByUserForm(FormAction):
    def name(self) -> Text:
        return "commit_by_user_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if (tracker.get_slot("bitbucket_action")):
        #     if ("watchers" in tracker.get_slot("bitbucket_action") or "list of watchers" in tracker.get_slot("bitbucket_action")):   
        #         return ["bitbucket_action","repo_name","owner_name"]
        # if (tracker.get_slot("search_keys")):
        #     if ("who" or "who all" in tracker.get_slot("search_keys")):
        #         return ["bitbucket_action","repo_name","owner_name"]
        return ["repo_name","owner_name","user_name"]



    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_commit_by_user(tracker.get_slot('repo_name'),
                                                tracker.get_slot('owner_name'), tracker.get_slot('user_name'))

        returnAnswer['type'] = 'bitbucket'
        txt = json.dumps(returnAnswer)
        dispatcher.utter_message(text=txt)
        return []
class CommitByBranchForm(FormAction):
    def name(self) -> Text:
        return "commit_by_branch_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if (tracker.get_slot("bitbucket_action")):
        #     if ("watchers" in tracker.get_slot("bitbucket_action") or "list of watchers" in tracker.get_slot("bitbucket_action")):   
        #         return ["bitbucket_action","repo_name","owner_name"]
        # if (tracker.get_slot("search_keys")):
        #     if ("who" or "who all" in tracker.get_slot("search_keys")):
        #         return ["bitbucket_action","repo_name","owner_name"]
        return ["repo_name","owner_name","branch_name"]
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_commit_by_branch(tracker.get_slot('repo_name'),
                                                tracker.get_slot('owner_name'), tracker.get_slot('branch_name'))

        returnAnswer['type'] = 'bitbucket'
        txt = json.dumps(returnAnswer)
        dispatcher.utter_message(text=txt)
        return []

class CommitMsgForm(FormAction):
    def name(self) -> Text:
        return "commit_msg_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if (tracker.get_slot("bitbucket_action")):
        #     if ("watchers" in tracker.get_slot("bitbucket_action") or "list of watchers" in tracker.get_slot("bitbucket_action")):   
        #         return ["bitbucket_action","repo_name","owner_name"]
        # if (tracker.get_slot("search_keys")):
        #     if ("who" or "who all" in tracker.get_slot("search_keys")):
        #         return ["bitbucket_action","repo_name","owner_name"]
        return ["repo_name","owner_name","message"]



    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_commit_by_msg(tracker.get_slot('repo_name'),
                                                tracker.get_slot('owner_name'), tracker.get_slot('message'))

        returnAnswer['type'] = 'bitbucket'
        txt = json.dumps(returnAnswer)
        dispatcher.utter_message(text=txt)
        return []

class WatcherListForm(FormAction):
    def name(self) -> Text:
        return "watcher_list_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["repo_name","owner_name"]
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_watchers(tracker.get_slot('repo_name'),tracker.get_slot('owner_name'))
        returnAnswer['type'] = 'bitbucket'
        txt = json.dumps(returnAnswer)
        dispatcher.utter_message(text=txt)
        return []

class ErrorSearchForm(FormAction):

    def __init__(self):
        self.error_query = ""
    def name(self) -> Text:
        return "error_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["error_query"]
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        obj = searchStack()
        returnVar = {}
        returnVar['reply'] = obj.searchStack(tracker.get_slot("error_query"))
        returnVar['status'] = 200
        returnVar['type'] = 'stackoverflow'
        returnVar = json.dumps(returnVar)
        dispatcher.utter_message(text=returnVar)
        return []


class BranchListForm(FormAction):

    def name(self):
        return "branch_list_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["repo_name","owner_name"]
    
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_branches(tracker.get_slot('repo_name'),tracker.get_slot('owner_name'))
        returnAnswer['type'] = 'bitbucket'
        txt = json.dumps(returnAnswer)
        dispatcher.utter_message(text=txt)
        return []

class RepoListForm(FormAction):

    def name(self):
        return "repo_list_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["owner_name"]
    
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        print (f"Target Repo: {tracker.get_slot('owner_name')}")
        returnAnswer = obj.get_repos(tracker.get_slot('owner_name'))
        returnAnswer['type'] = 'bitbucket'
        txt = json.dumps(returnAnswer)
        dispatcher.utter_message(text=txt)
        return []


# Information about all the spaces
class InfoAllSpaces(Action):

    def name(self) -> Text:
        return "action_info_of_all_spaces"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        t = get_all_spaces()
        tx = json.dumps(t, indent=4)
        txt = json.loads(tx)

        dispatcher.utter_message(text=txt)

        return []


# Create a new space
class CreateSpace(FormAction):

    def name(self) -> Text:
        return "create_space_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"space": [self.from_entity(entity="space"),
                            self.from_text()],
                "key": [self.from_entity(entity="key"),
                            self.from_text()]}


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["key", "space"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        #dispatcher.utter_message(text="Kya baat hai!!")
        #dispatcher.utter_message(template="utter_submit")

        a = str(tracker.get_slot('key'))
        b = str(tracker.get_slot('space'))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            create_space(a, b)
            
            #return [t]

        #t = 
        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        # txt = json.loads(t)
        dispatcher.utter_message(text="Space Created")
        return []

# Info of a specific space
class InfoSpace(Action):

    def name(self) -> Text:
        return "action_space_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = str(tracker.get_slot("key"))
        t = get_info_space(a)
        tx = json.dumps(t, indent = 2)
        txt = json.loads(tx)

        dispatcher.utter_message(text=txt)

        return []        


# Get pages in a space
class GetPagesInSpace(Action):

    def name(self) -> Text:
        return "action_get_pages_in_a_space"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = str(tracker.get_slot("space"))
        t = get_pages_in_a_space(a)
        tx = json.dumps(t, indent=4)
        txt = json.loads(tx)

        dispatcher.utter_message(text=txt)

        return []


# Create a new page
class CreatePage(FormAction):

    def name(self) -> Text:
        return "create_page_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"space": [self.from_entity(entity="space"),
                            self.from_text()],
                "title": [self.from_entity(entity="title"),
                            self.from_text()],
                "body": [self.from_entity(entity="body", intent="body_entry"),
                            self.from_text()]}

    # def validate_body(
    #         self, value:Text,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:



    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["space", "title", "body"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        #dispatcher.utter_message(text="Kya baat hai!!")
        #dispatcher.utter_message(template="utter_submit")

        a = str(tracker.get_slot('space'))
        b = str(tracker.get_slot('title'))
        c = str(tracker.get_slot("body"))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            create_page(a, b, c)
            
            #dispatcher.utter_message(text="Page Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        dispatcher.utter_message(text="Page Created")
        return []


# Delete a Page
class DeletePage(Action):

    def name(self) -> Text:
        return "action_delete_page"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = int(str(tracker.get_slot("page_id")))
        delete_page(a)

        dispatcher.utter_message(text="Page Deleted")

        return []





# Get Page info using id
class GetPageInfoById(Action):

    def name(self) -> Text:
        return "action_get_page_info_by_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = int(str(tracker.get_slot("page_id")))
        t = page_info_by_id(a)
        tx = json.dumps(t, indent = 2)
        txt = json.loads(tx)
        dispatcher.utter_message(text=txt)

        return []



# Export Page as PDF
class ExportPageAsPdf(FormAction):

    def name(self) -> Text:
        return "export_page_as_pdf_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"page_id": [self.from_entity(entity="page_id"),
                            self.from_text()],
                "file_name": [self.from_entity(entity="file_name"),
                            self.from_text()]}


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["page_id", "file_name"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        #dispatcher.utter_message(text="Kya baat hai!!")
        #dispatcher.utter_message(template="utter_submit")

        a = str(tracker.get_slot('page_id'))
        b = str(tracker.get_slot('file_name'))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            export_page_as_pdf(a, b)
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        dispatcher.utter_message(text="Page Exported")
        return []


class GetUserAllProject(FormAction):

    def name(self) -> Text:
        return "get_all_project_name_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return []

    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_all_project_name()
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []


class GetUserInGroup(FormAction):

    def name(self) -> Text:
        return "get_user_in_group_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['group_name']

    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_users_in_group(tracker.get_slot('group_name'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetIssueProject(FormAction):

    def name(self) -> Text:
        return "get_issue_in_project_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['project_name']

    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issues_in_project(tracker.get_slot('project_name'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []
        

class GetIssue(FormAction):

    def name(self) -> Text:
        return "get_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issue(tracker.get_slot('issue_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetEpic(FormAction):

    def name(self) -> Text:
        return "get_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issue(tracker.get_slot('epic_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetTask(FormAction):

    def name(self) -> Text:
        return "get_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issue(tracker.get_slot('task_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetStatusOfIssue(FormAction):

    def name(self) -> Text:
        return "get_status_of_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_status_of_issue(tracker.get_slot('issue_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetStatusOfEpic(FormAction):

    def name(self) -> Text:
        return "get_status_of_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_status_of_issue(tracker.get_slot('epic_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetStatusOfTask(FormAction):

    def name(self) -> Text:
        return "get_status_of_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_status_of_issue(tracker.get_slot('task_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetIssueVersion(FormAction):

    def name(self) -> Text:
        return "get_issue_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issue_version(tracker.get_slot('issue_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetEpicVersion(FormAction):

    def name(self) -> Text:
        return "get_epic_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issue_version(tracker.get_slot('epic_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetTaskVersion(FormAction):

    def name(self) -> Text:
        return "get_task_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_issue_version(tracker.get_slot('task_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetCommentIssue(FormAction):

    def name(self) -> Text:
        return "get_comment_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_comments_in_issue(tracker.get_slot('issue_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetCommentEpic(FormAction):

    def name(self) -> Text:
        return "get_comment_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_comments_in_issue(tracker.get_slot('epic_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetCommentTask(FormAction):

    def name(self) -> Text:
        return "get_comment_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_comments_in_issue(tracker.get_slot('task_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetWorklogIssue(FormAction):

    def name(self) -> Text:
        return "get_worklog_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_worklog_in_issue(tracker.get_slot('issue_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetWorklogTask(FormAction):

    def name(self) -> Text:
        return "get_worklog_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_worklog_in_issue(tracker.get_slot('task_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []

class GetWorklogEpic(FormAction):

    def name(self) -> Text:
        return "get_worklog_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        ret_data = get_worklog_in_issue(tracker.get_slot('epic_summary'))
        txt = json.dumps(ret_data)
        dispatcher.utter_message(text=txt)
        return []


class GetLatestInboxEmail(Action):

    def name(self) -> Text:
        return "action_get_latest_email_in_inbox"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        op = int(tracker.latest_message.get('text'))
        t = LatestMailInInbox(op)
        # tx = json.dumps(t, indent = 4)
        # txt = json.loads(tx)
        # txtt = json.dumps(txt, indent = 2)
        
        dispatcher.utter_message(text=t)

        return []


class GetLatestUserEmail(Action):

    def name(self) -> Text:
        return "action_get_latest_email_from_user"

    # @staticmethod
    # def required_slots(tracker: Tracker) -> List[Text]:
    #     """ The required entries for this function """

    #     print("required_slots(tracker : Tracker)")
    #     return ["query"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        q = str(tracker.get_slot("query"))
        op = int(tracker.latest_message.get('text'))
        t = GetLatestMailFromUser(q, op)
        #tx = json.dumps(t, indent = 4)
        # txt = json.loads(tx)
        # txtt = json.dumps(txt, indent = 2)
        
        dispatcher.utter_message(text=t)

        return []        



class GetLatestLabelEmail(Action):

    def name(self) -> Text:
        return "action_get_latest_email_from_label"

    # @staticmethod
    # def required_slots(tracker: Tracker) -> List[Text]:
    #     """ The required entries for this function """

    #     print("required_slots(tracker : Tracker)")
    #     return ["query"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        q = str(tracker.get_slot("query"))
        op = int(tracker.latest_message.get('text'))
        t = GetLatestMailFromLabel(q, op)
        #tx = json.dumps(t, indent = 4)
        # txt = json.loads(tx)
        # txtt = json.dumps(txt, indent = 2)
        
        dispatcher.utter_message(text=t)

        return [] 


class SendEmail(FormAction):

    def name(self) -> Text:
        return "send_email_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"email_body": [self.from_entity(entity="email_body"),
                            self.from_text()],
                "receiver": [self.from_entity(entity="receiver"),
                            self.from_text()],
                "subject": [self.from_entity(entity="subject"),
                            self.from_text()]}

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["receiver", "subject", "email_body"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        a = str(tracker.get_slot("email_body"))
        b = str(tracker.get_slot("receiver"))
        c = str(tracker.get_slot("subject"))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            SendMail(a, b, c)
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        dispatcher.utter_message(text="Email Sent")

        return []


class SendEmailWithAttachments(FormAction):

    def name(self) -> Text:
        return "send_email_with_attachments_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"email_body": [self.from_entity(entity="email_body"),
                            self.from_text()],
                "receiver": [self.from_entity(entity="receiver"),
                            self.from_text()],
                "subject": [self.from_entity(entity="subject"),
                            self.from_text()],
                "file_dir": [self.from_entity(entity="file_dir"),
                            self.from_text()],
                "filename": [self.from_entity(entity="filename"),
                            self.from_text()]}

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["receiver", "subject", "email_body", "file_dir", "filename"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        a = str(tracker.get_slot("email_body"))
        b = str(tracker.get_slot("receiver"))
        c = str(tracker.get_slot("subject"))
        d = str(tracker.get_slot("file_dir"))
        e = str(tracker.get_slot("filename"))


        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            SendMailWithAttachments(a, b, c, d, e)
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        dispatcher.utter_message(text="Email Sent")

        return []        
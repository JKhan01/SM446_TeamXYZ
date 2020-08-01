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

obj = bitbucketActions()


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

        txt = ',\n'.join(returnAnswer['reply'])
        dispatcher.utter_message(text=txt)
        return []



class CommitForm(FormAction):

    def name(self) -> Text:
        return "commit_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if (tracker.get_slot("bitbucket_action")):
        #     if ("watchers" in tracker.get_slot("bitbucket_action") or "list of watchers" in tracker.get_slot("bitbucket_action")):   
        #         return ["bitbucket_action","repo_name","owner_name"]
        # if (tracker.get_slot("search_keys")):
        #     if ("who" or "who all" in tracker.get_slot("search_keys")):
        #         return ["bitbucket_action","repo_name","owner_name"]
        return ["bitbucket_action","repo_name","owner_name","user_name","branch_name"]



    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_commit_by_user(tracker.get_slot('repo_name'),tracker.get_slot('owner_name'),tracker.get_slot('user_name'))
        txt = ',\n'.join(returnAnswer['reply'])
        dispatcher.utter_message(text=txt)
        return []
        

class WatchersForm(FormAction):
    def name(self) -> Text:
        return "watchers_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["repo_name","owner_name"]
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        
        returnAnswer = obj.get_watchers(tracker.get_slot('repo_name'),tracker.get_slot('owner_name'))
        txt = ',\n'.join(returnAnswer['reply'])
        dispatcher.utter_message(text=txt)
        return []


class ErrorForm(FormAction):

    def __init__(self):
        self.error_query = ""
    def name(self) -> Text:
        return "error_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["error_action"]
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        self.error_query = tracker.get_slot("error_action")
        obj = searchStack()
        returnVar = obj.searchStack(self.error_query)
        dispatcher.utter_message(text=returnVar)
        return []


class BranchForm(FormAction):

    def name(self):
        return "branch_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["repo_name","owner_name"]
    
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        returnAnswer = obj.get_branches(tracker.get_slot('repo_name'),tracker.get_slot('owner_name'))
        txt = ',\n'.join(returnAnswer['reply'])
        dispatcher.utter_message(text=txt)
        return []


class RepoForm(FormAction):

    def name(self):
        return "repo_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["owner_name"]
    
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        print (f"Target Repo: {tracker.get_slot('owner_name')}")
        returnAnswer = obj.get_repos(tracker.get_slot('owner_name'))
        txt = ',\n'.join(returnAnswer['reply'])
        dispatcher.utter_message(text=txt)
        return []


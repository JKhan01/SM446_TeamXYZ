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

class EpicCreate(FormAction):

    def name(self) -> Text:
        return "create_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name','issue_type','version_entity','description_entity','issue_summary','epic_name','assignee_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []



class StoryCreate(FormAction):

    def name(self) -> Text:
        return "create_story_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name','issue_type','version_entity','description_entity','issue_summary','assignee_name','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class BugCreate(FormAction):

    def name(self) -> Text:
        return "create_bug_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name','issue_type','version_entity','description_entity','issue_summary','assignee_name','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class TaskCreate(FormAction):

    def name(self) -> Text:
        return "create_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name','issue_type','version_entity','description_entity','issue_summary','assignee_name','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class SubTaskCreate(FormAction):

    def name(self) -> Text:
        return "create_subtask_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name','issue_type','version_entity','description_entity','issue_summary','assignee_name','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class VersionCreate(FormAction):

    def name(self) -> Text:
        return "create_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['version_entity','start_date','release_date','description_entity','project_name','released_status']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class ProjectCreate(FormAction):

    def name(self) -> Text:
        return "create_project_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name','project_template','temp_type','project_key','description_entity','project_lead']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []


class GroupCreate(FormAction):

    def name(self) -> Text:
        return "create_group_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['group_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class AddUserToGroup(FormAction):

    def name(self) -> Text:
        return "add_user_to_group_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['user_name','group_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []


class GetUserInGroup(FormAction):

    def name(self) -> Text:
        return "get_user_in_group_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['group_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetIssueInProject(FormAction):

    def name(self) -> Text:
        return "get_issue_in_project_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['project_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetIssue(FormAction):

    def name(self) -> Text:
        return "get_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []


class GetStatusOfIssue(FormAction):

    def name(self) -> Text:
        return "get_status_of_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetIssueVersion(FormAction):

    def name(self) -> Text:
        return "get_issue_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []


class AddComment(FormAction):

    def name(self) -> Text:
        return "add_comment_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','comment','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []



class DeleteComment(FormAction):

    def name(self) -> Text:
        return "delete_comment_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['comment','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetComment(FormAction):

    def name(self) -> Text:
        return "get_comment_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []


class AddWorklog(FormAction):

    def name(self) -> Text:
        return "add_worklog_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','worklog','issue_summary','week','day','hour','minute']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class DeleteWorklog(FormAction):

    def name(self) -> Text:
        return "delete_worklog_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['worklog','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetWorklog(FormAction):

    def name(self) -> Text:
        return "get_worklog_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []
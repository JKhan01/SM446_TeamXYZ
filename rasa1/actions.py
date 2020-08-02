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
        return ['epic_name','epic_summary','description_entity','version_entity','project_name','issue_type','assignee_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []



class StoryCreate(FormAction):

    def name(self) -> Text:
        return "create_story_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary','description_entity','version_entity','project_name','issue_type','epic_summary','assignee_name']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class BugCreate(FormAction):

    def name(self) -> Text:
        return "create_bug_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary','description_entity','version_entity','project_name','issue_type','epic_summary','assignee_name']
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class TaskCreate(FormAction):

    def name(self) -> Text:
        return "create_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['task_summary','description_entity','version_entity','project_name','issue_type','epic_summary','assignee_name']
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class SubTaskCreate(FormAction):

    def name(self) -> Text:
        return "create_subtask_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary','description_entity','version_entity','project_name','issue_type','task_summary','assignee_name']
    
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
        return ['project_template','temp_type','project_name','project_key','description_entity','project_lead']
    
    
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

class GetEpic(FormAction):

    def name(self) -> Text:
        return "get_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetTask(FormAction):

    def name(self) -> Text:
        return "get_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
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

class GetStatusOfEpic(FormAction):

    def name(self) -> Text:
        return "get_status_of_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetStatusOfTask(FormAction):

    def name(self) -> Text:
        return "get_status_of_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
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

class GetEpicVersion(FormAction):

    def name(self) -> Text:
        return "get_epic_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetTaskVersion(FormAction):

    def name(self) -> Text:
        return "get_task_version_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class AddCommentIssue(FormAction):

    def name(self) -> Text:
        return "add_comment_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','comment','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class AddCommentEpic(FormAction):

    def name(self) -> Text:
        return "add_comment_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','comment','epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class AddCommentTask(FormAction):

    def name(self) -> Text:
        return "add_comment_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','comment','task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

        



class DeleteCommentIssue(FormAction):

    def name(self) -> Text:
        return "delete_comment_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['comment','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class DeleteCommentTask(FormAction):

    def name(self) -> Text:
        return "delete_comment_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['comment','task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class DeleteCommentEpic(FormAction):

    def name(self) -> Text:
        return "delete_comment_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['comment','epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetCommentIssue(FormAction):

    def name(self) -> Text:
        return "get_comment_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetCommentEpic(FormAction):

    def name(self) -> Text:
        return "get_comment_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetCommentTask(FormAction):

    def name(self) -> Text:
        return "get_comment_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []


class AddWorklogIssue(FormAction):

    def name(self) -> Text:
        return "add_worklog_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','worklog','issue_summary','week','day','hour','minute']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class AddWorklogTask(FormAction):

    def name(self) -> Text:
        return "add_worklog_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','worklog','task_summary','week','day','hour','minute']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class AddWorklogEpic(FormAction):

    def name(self) -> Text:
        return "add_worklog_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['visible_to_role','worklog','epic_summary','week','day','hour','minute']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class DeleteWorklogIssue(FormAction):

    def name(self) -> Text:
        return "delete_worklog_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['worklog','issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class DeleteWorklogEpic(FormAction):

    def name(self) -> Text:
        return "delete_worklog_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['worklog','epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class DeleteWorklogTask(FormAction):

    def name(self) -> Text:
        return "delete_worklog_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['worklog','task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetWorklogIssue(FormAction):

    def name(self) -> Text:
        return "get_worklog_issue_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['issue_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetWorklogTask(FormAction):

    def name(self) -> Text:
        return "get_worklog_task_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['task_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []

class GetWorklogEpic(FormAction):

    def name(self) -> Text:
        return "get_worklog_epic_form"
    ## return the same form name
    
    @staticmethod
    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ['epic_summary']
    
    
    def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(text="Parameters Submitted")
        return []
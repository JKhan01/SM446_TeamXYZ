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
from rasa_sdk.events import SlotSet

from functions import *
from g5 import *
from g6 import *

slotList = ["space", "key", "body", "page_id", "title", "file_name", "body", "receiver", "subject", "query"]
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


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



        a = str(tracker.get_slot('key'))
        b = str(tracker.get_slot('space'))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            create_space(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
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


# Check Page exists
class CheckPageExists(FormAction):

    def name(self) -> Text:
        return "check_page_exists_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"space": [self.from_entity(entity="space"),
                            self.from_text()],
                "title": [self.from_entity(entity="title"),
                            self.from_text()]}


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["space", "title"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        #dispatcher.utter_message(text="Kya baat hai!!")
        #dispatcher.utter_message(template="utter_submit")

        a = str(tracker.get_slot('space'))
        b = str(tracker.get_slot('title'))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            t = check_page_exists(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return [t]

        t = run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        tx = json.dumps(t, indent = 4)
        txt = json.dumps(tx)
        dispatcher.utter_message(text=txt)
        return []


# Get page id
class GetPageId(FormAction):

    def name(self) -> Text:
        return "get_page_id_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"space": [self.from_entity(entity="space"),
                            self.from_text()],
                "title": [self.from_entity(entity="title"),
                            self.from_text()]}


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["space", "title"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        #dispatcher.utter_message(text="Kya baat hai!!")
        #dispatcher.utter_message(template="utter_submit")

        a = str(tracker.get_slot('space'))
        b = str(tracker.get_slot('title'))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            t = get_page_id(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return [t]

        t = run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        tx = json.dumps(t)
        
        dispatcher.utter_message(text=tx)
        return []


# Get Page space
class GetPageSpace(Action):

    def name(self) -> Text:
        return "action_get_page_space"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = int(str(tracker.get_slot("page_id")))
        t = get_page_space(a)
        tx = json.dumps(t)
        #txt = json.dumps(tx)

        dispatcher.utter_message(text=tx)

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


# Get page info by title
class GetPageInfoByTitle(FormAction):

    def name(self) -> Text:
        return "get_page_info_by_title_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {"space": [self.from_entity(entity="space"),
                            self.from_text()],
                "title": [self.from_entity(entity="title"),
                            self.from_text()]}


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["space", "title"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        #dispatcher.utter_message(text="Kya baat hai!!")
        #dispatcher.utter_message(template="utter_submit")

        a = str(tracker.get_slot('space'))
        b = str(tracker.get_slot('title'))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            t = page_info_by_title(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return [t]

        t = run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        tx = json.dumps(t, indent = 2)
        txt = json.loads(tx)
        txtt = json.dumps(txt)
        dispatcher.utter_message(text=txtt)
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
            
            #dispatcher.utter_message(text="Space Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        dispatcher.utter_message(text="Page Exported")
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

        return {"body": [self.from_entity(entity="body"),
                            self.from_text()],
                "receiver": [self.from_entity(entity="receiver"),
                            self.from_text()],
                "subject": [self.from_entity(entity="subject"),
                            self.from_text()]}

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ The required entries for this function """

        print("required_slots(tracker : Tracker)")
        return ["receiver", "subject", "body"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        a = str(tracker.get_slot("body"))
        b = str(tracker.get_slot("receiver"))
        c = str(tracker.get_slot("subject"))

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            SendMail(a, b, c)
            
            return []

        dispatcher.utter_message(text="Email Sent")

        return []



class SendEmailWithAttachments(Action):

    def name(self) -> Text:
        return "action_send_email_with_attachments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SendMailWithAttachments()

        dispatcher.utter_message(text="Email Sent")

        return []
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


slotList = ["space", "key", "body", "page_id", "title", "file_name"]

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

        get_all_spaces()

        dispatcher.utter_message(text="Done")

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
            
            #dispatcher.utter_message(text="Space Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        return [] 

    
# Info of a specific space
class InfoSpace(Action):

    def name(self) -> Text:
        return "action_space_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = str(tracker.get_slot("key"))
        get_info_space(a)

        #dispatcher.utter_message(text="Done")

        return []        


# Get pages in a space
class GetPagesInSpace(Action):

    def name(self) -> Text:
        return "action_get_pages_in_a_space"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = str(tracker.get_slot("space"))
        get_pages_in_a_space(a)

        #dispatcher.utter_message(text="Done")

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

            check_page_exists(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
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

            get_page_id(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
        return []


# Get Page space
class GetPageSpace(Action):

    def name(self) -> Text:
        return "action_get_page_space"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = int(str(tracker.get_slot("page_id")))
        get_page_space(a)

        #dispatcher.utter_message(text="Page Deleted")

        return []


# Get Page info using id
class GetPageInfoById(Action):

    def name(self) -> Text:
        return "action_get_page_info_by_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = int(str(tracker.get_slot("page_id")))
        page_info_by_id(a)

        #dispatcher.utter_message(text="Page Deleted")

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

            page_info_by_title(a, b)
            
            #dispatcher.utter_message(text="Space Created")
            
            return []

        run(self, CollectingDispatcher, Tracker, Dict[Text, Any])
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
        return []
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
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

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World! This is my bot")

        return []

class ActionCovidTracker(Action):

    def name(self) -> Text:
        return "action_covid19_status_tracker"
    

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response= requests.get("https://api.covid19india.org/data.json").json()
        entity=tracker.latest_message['entities']
        print("Entity for last messagein state ",entity)
        print_msg="Please correct State name"
        state=None
        
        for e in entity:
            if e['entity']=="state":
                state=e['value']
        for data in response["statewise"]:
            if data['state']==state.title():
                print(data)
                print_msg= "Active: "+data["active"]+"\n"+"Confirmed: "+data['confirmed']+"\n"+"Recovered: "+data['recovered']+"\n"+"As of: "+data['lastupdatedtime']
        next_response="\nEnter district name to know its status"
        print("Last entity: ",entity)
        state=None
            
        dispatcher.utter_message(text=print_msg+next_response)

        return []
    
class ActionCovidZoneTracker(Action):

    def name(self) -> Text:
        return "action_covid19_zone_status"
    

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response= requests.get("https://api.covid19india.org/zones.json").json()
        entity=tracker.latest_message['entities']
        print("Entity for last message",entity)
        print_msg="Please correct district name"
        district=None
        district_lookup=['']
        for e in entity:
            if e['entity'] in ["district","state"]:
                district=e['value']
        for data in response["zones"]:
            if data['district'].lower()==district.lower():
                print(data)
                print_msg= district+" is in "+data['zone']+"\n"+"As of: "+data['lastupdated']
        #next_response="\nEnter district name to know its status\n Nalgonda is in which zone"
        print("Last entity: ",entity)
        district=None
            
        dispatcher.utter_message(text=print_msg)

        return []


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hey,How are you? Welcome to Marble store. ")
        # dispatcher.utter_message(image = "https://thumbs.dreamstime.com/b/stone-marble-background-abstract-marbel-design-wall-floor-beautiful-grey-curly-golden-veins-161430363.jpg")

        return []

class ActionLocationResponse(Action):

    def name(self) -> Text:
        return "action_location_response"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        print(len(entities))
        for e in entities:
            if e['entity'] == 'location':
                name = e['value']
            if name == 'karachi':
                message = "order will be deliverd in 5 days"
            if name == 'islamabad':
                message = "order will be delivered in 24 hours"
            if name == 'rawalpindi':
                message = "order will be delivered in 24 hours."

        dispatcher.utter_message(text=f"in {name} {message}")
        return []

class ActionsizeResponse(Action):

    def name(self) -> Text:
        return "action_size_response"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        print(len(entities))
        values = []
        for e in entities:
            if e['entity'] == 'size':
                values.append(e['value'])
        a = int(values[0])
        b = int(values[1])
        total_size = a * b
        total_cost = total_size * 7
        dispatcher.utter_message(text=f"Total size of floor is {total_size}, and cost is {total_cost}$")
        return []

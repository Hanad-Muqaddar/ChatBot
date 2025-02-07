# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionLocationResponse(Action):

    def name(self) -> Text:
        return "action_location_response"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'location':
                n = e['value']
                name = n.lower()
            if name == 'atlanta':
                message = " Atlanta order will be deliverd in 2 days"
            elif name == 'brossard':
                message = "Brossard order will be delivered in 24 hours"
            elif name == 'toronto':
                message = "Toronto order will be delivered in 3 days."
            elif name == 'detroit':
                message = "Detroit order will be delivered in 24 hours."
            elif name == 'montreal':
                message = "Montreal order will be delivered in 4 days."
            else:
                message = "this location we don't operate."

        dispatcher.utter_message(text=f"In {message}")
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
        dispatcher.utter_message(text=f"Total floor size is {total_size} square feet, and cost is ${total_cost}")
        return []

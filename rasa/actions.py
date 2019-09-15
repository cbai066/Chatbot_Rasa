# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from  features.weather import get_weather
from  features.weather import weather_info

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        current = get_weather(loc)

        city, country, weather, t, maxt, mint, humidity, pressure = weather_info(current)
        response = 'city:     {}\ncountry:     {}\nweather:     {}\ntemperature:    {} ℃\nMax_temperature:    {} ' \
                   '℃\nMin_temperature:    {} ℃\nhumidity:   {} \npressure:   {} \n'.format(
                    city, country, weather, t, maxt, mint, humidity, pressure)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]
'''
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Hello World!")

         return []
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key="d1881979fb4d4ee4879110427182103"
        client=ApixuClient(api_key)
        loc=tracker.get_slot('location')
        current = client.getCurrentWeather(loc)
        country=current['location']['country']
        city=current['location']['name']
        condition=current['current']['condition']['text']
        temperatur=current['current']['temp_c']
        humudity=current['current']['humidity']
        wind_mph=current['current']['wind_mph']
        response="""
        It is currently {} in {} at the moment. The remperatur is {} degrees,
        the humidity is {}% and wind speed is {} mph.
        """.format(condition,city,temperatur,humudity,wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]
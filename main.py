import requests
import urllib.parse as urllib
import json
from timeit import default_timer as timer
import time

keys = open("keys.json", "r").read()
keys = json.loads(keys)

BASE_API_URL = "https://api.groupme.com/v3"
TOKEN_URL  = BASE_API_URL + "/groups?token="


def event_checker():
    start = timer()
    events = open("events.json", "r").read()
    events = json.loads(events)
    keys = open("keys.json", "r").read()
    keys = json.loads(keys)
    today = time.strftime("%d%m%Y")
    try:
        message = "Events today (" + time.strftime("%m/%d/%Y") + "):\n"
        try:
            for event in events[today]["Events"]:
                new_message = event + " at " + events[today]["Events"][event]["Time"]
                location = events[today]["Events"][event]["Location"]
                message += new_message + ", located at " + location + "\n"
                try:
                    message += "Itinerary:\n"
                    for label in events[today]["Events"][event]["Itinerary"]:
                        message += label + "\n"
                except KeyError:
                    pass
                message += "\n"
        except KeyError:
            new_message = events[today]["Events"]
            message += new_message
        final_message = urllib.quote_plus(message)
        print(message)
        requests.post(BASE_API_URL + "/bots/post?bot_id=" + keys["bot_id"] + "&text=" + final_message)
    except KeyError:
        string = "gabe pleas ubpate the events"
        string = urllib.quote_plus(string)
        print(string)
        requests.post(BASE_API_URL + "/bots/post?bot_id=" + keys["bot_id"] + "&text=" + string)
    end = timer()
    print("Time: %s ms" % str((end - start)))

event_checker()
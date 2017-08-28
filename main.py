import requests
import oauth2client
import asyncio
import websockets
import json
from threading import Timer
import time

keys = open("keys.json", "r")

OAUTH2_URL = "https://oauth.groupme.com/oauth/authorize?client_id="
BASE_API_URL = "https://api.groupme.com/v3"

AUTH_URL = OAUTH2_URL + keys.json()
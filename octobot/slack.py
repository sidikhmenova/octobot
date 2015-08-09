import sys
import requests
import json


def incoming_web_hook(url, text, username, channel, icon_emoji):
    payload = {
        'text': text,
        'username': username,
        'channel': channel,
        'icon_emoji': icon_emoji
    }

    try:
        requests.post(url, data=json.dumps(payload))
        return 0
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

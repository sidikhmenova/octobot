import requests
import json


def incoming_web_hook(url, text, username, channel, icon_emoji):
    payload = {
        'text': text,
        'username': username,
        'channel': channel,
        'icon_emoji': icon_emoji
    }

    # print(url)
    # print(payload)
    return requests.post(url, data=json.dumps(payload))

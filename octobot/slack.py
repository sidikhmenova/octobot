import requests
import json


def incoming_web_hook(url, text, username, channel, icon_emoji):
    payload = {
        url: url,
        text: text,
        username: username,
        channel: channel,
        icon_emoji: icon_emoji
    }

    return requests.post(url, data=json.dumps(payload))

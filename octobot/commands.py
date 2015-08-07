from octobot.utils import config_data_to_incoming_webhook_args
from octobot.slack import incoming_web_hook


def says(config):
    args = config_data_to_incoming_webhook_args(config.data)
    incoming_web_hook(*args)


def get(key):
    map = {
        'says': says
    }

    return map.get(key, None)

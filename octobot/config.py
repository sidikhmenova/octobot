import os
from confypy import Config
from confypy import Location

yamlConf = '.octobot/config.yaml'
ud = os.path.expanduser('~')
cwd = os.getcwd()
user_config = os.path.join(ud, yamlConf)
local_config = os.path.join(cwd, yamlConf)

env_keys = [
    'OCTOBOT_INCOMING_WEBHOOK_URL',
    'OCTOBOT_USERNAME',
    'OCTOBOT_CHANNEL',
    'OCTOBOT_ICON_EMOJI'
]

defaults = {
    'OCTOBOT_INCOMING_WEBHOOK_URL': None,
    'OCTOBOT_MESSAGE': None,
    'OCTOBOT_USERNAME': 'octobot',
    'OCTOBOT_CHANNEL': 'general',
    'OCTOBOT_ICON_EMOJI': ':octopus:'
}


def load_config(overrides):
    config = Config(chain=True, defaults=defaults)

    config.locations = [
        Location.from_env_keys(env_keys),
        Location.from_path(user_config),
        Location.from_path(local_config),
        Location.from_dict(overrides),
    ]

    return config

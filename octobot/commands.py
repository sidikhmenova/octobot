from octobot.utils import parse_arguments
from octobot.slack import incoming_web_hook


def say_message(config, arguments):
    parsed_arguments = parse_arguments(arguments)
    url              = config.data.OCTOBOT_INCOMING_WEBHOOK_URL
    username         = config.data.OCTOBOT_USERNAME
    channel          = config.data.OCTOBOT_CHANNEL
    icon_emoji       = config.data.OCTOBOT_ICON_EMOJI
    message          = parsed_arguments['message']

    return incoming_web_hook(
        url,
        message,
        username,
        channel,
        icon_emoji
    )


def say_aliased_message(config, arguments):
    parsed_arguments = parse_arguments(arguments)
    url              = config.data.OCTOBOT_INCOMING_WEBHOOK_URL
    username         = config.data.OCTOBOT_USERNAME
    channel          = config.data.OCTOBOT_CHANNEL
    icon_emoji       = config.data.OCTOBOT_ICON_EMOJI
    alias            = parsed_arguments['alias']
    aliases          = config.data.OCTOBOT_ALIASES
    aliased_message  = None

    try:
        aliased_message = aliases[alias]
    except:
        print('Could not find alias for key: ' + alias)
        return -1

    return incoming_web_hook(
        url,
        aliased_message,
        username,
        channel,
        icon_emoji
    )

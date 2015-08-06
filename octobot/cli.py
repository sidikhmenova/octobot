"""Usage:
    octobot <msg> [options]

    Options:
        -u URL, --incoming-webhook-url <url>     Override incoming webhook url
        -n NAME, --username <name>               Override outgoing username
        -c CHANNEL, --channel <channel>          Override outgoing channel
        -i ICON, --icon-emoji <icon>             Override outgoing emoji

"""

from __future__ import print_function
import sys
from pprint import pprint

from docopt import docopt
from octobot import __version__
from octobot.config import load_config
from octobot.utils import parse_arguments
from octobot.utils import config_data_to_incoming_webhook_args


def main():
    arguments = docopt(
        __doc__, version=__version__
    )

    print('\narguments:')
    print(arguments)

    print('\nparsed arguments:')
    print(parse_arguments(**arguments))

    config = load_config(**parse_arguments(**arguments))

    print('\nconfig data:')
    print(config.data.OCTOBOT_INCOMING_WEBHOOK_URL)
    print(config.data.OCTOBOT_MESSAGE)
    print(config.data.OCTOBOT_USERNAME)
    print(config.data.OCTOBOT_CHANNEL)
    print(config.data.OCTOBOT_ICON_EMOJI)

    print('\nconfig.data')
    pprint(config.data.__dict__)

    print('\nwebhook args')
    print(config_data_to_incoming_webhook_args(config.data))


if __name__ == "__main__":
    sys.exit(main())

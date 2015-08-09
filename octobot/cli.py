"""Usage:
    octobot says <msg> [options]

    Options:
        -a ALIAS, --alias                        Override
        -u URL, --incoming-webhook-url <url>     Override incoming webhook url
        -n NAME, --username <name>               Override outgoing username
        -c CHANNEL, --channel <channel>          Override outgoing channel
        -i ICON, --icon-emoji <icon>             Override outgoing emoji

"""

from __future__ import print_function
import sys

from docopt import docopt
from octobot import __version__
from octobot.config import load_config
from octobot.utils import parse_arguments
from octobot.utils import print_debug

import octobot.commands as commands


def main():
    arguments = docopt(
        __doc__, version=__version__
    )

    parsed_args = parse_arguments(**arguments)
    config = load_config(parsed_args)

    try:
        config.data.OCTOBOT_DEBUG
        print_debug(arguments, parsed_args, config)
        return 0
    except:
        pass

    if arguments['says']:
        commands.get('says')(config)
        return 0


if __name__ == "__main__":
    sys.exit(main())

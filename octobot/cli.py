"""Usage:
    octobot says <msg> [options]
    octobot says (-a ALIAS | --alias <alias>) [options]

    Options:
        -a ALIAS, --alias                        Supplies key for aliased messages
        -u URL, --incoming-webhook-url <url>     Override incoming webhook url
        -n NAME, --username <name>               Override outgoing username
        -c CHANNEL, --channel <channel>          Override outgoing channel
        -i ICON, --icon-emoji <icon>             Override outgoing emoji

    Examples:

        $ octobot says 'Hello World'                                                    Send a custom message
        $ octobot says -a hello_world                                                   Send an aliased message:
        $ octobot says 'Howdy!' -u http://example.com -n cowboy -c #public -i :cowboy:  Send a custom message using all command-line options


"""

from __future__ import print_function
import sys

from docopt import docopt
from octobot import __version__
from octobot.config import load_config
from octobot.utils import config_overrides_from_arguments
from octobot.utils import print_debug

import octobot.commands as commands


def main():
    arguments = docopt(
        __doc__, version=__version__
    )

    config = load_config(config_overrides_from_arguments(arguments))

    try:
        config.data.OCTOBOT_DEBUG
        print_debug(config, arguments)
        return 0
    except:
        pass

    if arguments['<msg>']:
        return commands.say_message(config, arguments)

    if arguments['--alias']:
        return commands.say_aliased_message(config, arguments)


if __name__ == "__main__":
    sys.exit(main())

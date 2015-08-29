Octobot
=======

A light wrapper and configurable cli around Slack’s Incoming Web Hooks
API

Requirements
------------

> See *octobot/requirements/* for more info

    confypy==0.2.5
    docopt==0.6.2
    PyYAML==3.11
    requests==2.7.0

Installation
------------

> Until I get around publishing this into Pypi…

    # clone repo and..
    python setup.py install

About
-----

Octobot is a light wrapper around Slack’s Incoming Webhook API.

It supplies:

-   A convenient command line
-   A full set of command-line options
-   A convenient configuration convention

*See:* [Slack Incoming Webhook Docs]

Usage
-----

The current usage pattern looks like:

    Usage:
        octobot says <msg> [options]
        octobot says (-a ALIAS | --alias <alias>) [options]

        Options:
            -a ALIAS, --alias                        Supplies key for aliased messages
            -u URL, --incoming-webhook-url <url>     Override incoming webhook url
            -n NAME, --username <name>               Override outgoing username
            -c CHANNEL, --channel <channel>          Override outgoing channel
            -i ICON, --icon-emoji <icon>             Override outgoing emoji

### Command Examples

> Some examples may require some configuration to be in place (*see
> Configuration*)

Send a custom message:

    $ octobot says 'Hello World'

Send an aliased message:

    $ octobot says -a hello_world

Send a custom message using all command-line options:

    $ octobot says 'Howdy!' -u http://example.com -n cowboy -c #public -i :cowboy:

Configuration
-------------

Octobot is configurable and looks for config in the following places:

> Config values found at the top of the list override those found near
> the bottom.

-   Applicable command-line options
-   The local directory in: *.octobot/config.yaml*
-   The user directory in: *.octobot/config.yaml*
-   Environment variables

Configuration Variables:

    OCTOBOT_INCOMING_WEBHOOK_URL # slack webhook api option
    OCTOBOT_USERNAME             # slack webhook api option
    OCTOBOT_CHANNEL              # slack webhook api option
    OCTOBOT_ICON_EMOJI           # slack webhook api option
    OCTOBOT_ALIASES              # a list of alias keys and messages
    OCTOBOT_DEBUG                # any value enables some basic debugging

Sample *config.yaml*:

    # OCTOBOT_DEBUG: 'true'
    OCTOBOT_INCOMING_WEBHOOK_URL: 'http://example.com'
    OCTOBOT_USERNAME: 'octobots_evil_twin'
    OCTOBOT_CHANNEL: '#public'
    OCTOBOT_ICON_EMOJI': ':evil_octopus:'
    OCTOBOT_ALIASES:
        mantra: 'All Your Base Are Belong to Us'

Octobot comes with the following Incoming Webhook options set by
default:

-   **username:** octobot
-   **channel:** \#general
-   **icon\_emoji:** :octopus:

The only configuration parameter that is required is the:

    OCTOBOT_INCOMING_WEBHOOK_URL

  [Slack Incoming Webhook Docs]: https://api.slack.com/incoming-webhooks

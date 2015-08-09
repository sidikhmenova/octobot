def parse_arguments(arguments):
    parsed = {}
    parsed['message'] = arguments['<msg>']
    parsed['username'] = arguments['--username']
    parsed['channel'] = arguments['--channel']
    parsed['icon_emoji'] = arguments['--icon-emoji']
    parsed['incoming_webhook_url'] = arguments['--incoming-webhook-url']
    parsed['alias'] = arguments['--alias']

    return parsed


def config_overrides_from_arguments(arguments):
    parsed = {}
    parsed['OCTOBOT_USERNAME'] = arguments['--username']
    parsed['OCTOBOT_CHANNEL'] = arguments['--channel']
    parsed['OCTOBOT_ICON_EMOJI'] = arguments['--icon-emoji']
    parsed['OCTOBOT_INCOMING_WEBHOOK_URL'] = arguments['--incoming-webhook-url']

    return {k: v for k, v in parsed.iteritems() if v}


def print_debug(config, arguments):
    print('\nOctobot OCTOBOT_DEBUG flag is in enabled, printing debug info...')
    print('\narguments:')
    print(arguments)

    print('\nconfig.data')
    print(config.data.__dict__)
    print('\n')

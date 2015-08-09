def parse_arguments(**kwargs):
    parsed = {}
    parsed['OCTOBOT_MESSAGE'] = kwargs['<msg>']
    parsed['OCTOBOT_USERNAME'] = kwargs['--username']
    parsed['OCTOBOT_CHANNEL'] = kwargs['--channel']
    parsed['OCTOBOT_ICON_EMOJI'] = kwargs['--icon-emoji']
    parsed['OCTOBOT_INCOMING_WEBHOOK_URL'] = kwargs['--incoming-webhook-url']

    return {k: v for k, v in parsed.iteritems() if v}


def config_data_to_incoming_webhook_args(config_data):
    return [
        config_data.OCTOBOT_INCOMING_WEBHOOK_URL,
        config_data.OCTOBOT_MESSAGE,
        config_data.OCTOBOT_USERNAME,
        config_data.OCTOBOT_CHANNEL,
        config_data.OCTOBOT_ICON_EMOJI,
    ]


def print_debug(arguments, parsed_args, config):
    print('\nOctobot OCTOBOT_DEBUG flag is in enabled, printing debug info...')
    print('\narguments:')
    print(arguments)

    print('\nparsed_args:')
    print(parsed_args)

    print('\nconfig.data')
    print(config.data.__dict__)
    print('\n')

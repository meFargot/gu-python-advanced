from argparse import ArgumentParser

import yaml


DEFAULT_SERVER = 'localhost'
DEFAULT_PORT = 7777
DEFAULT_BUFFERSIZE = 1024


def get_config():
    parser = ArgumentParser()

    parser.add_argument(
        '-s', '--server', type=str, required=False,
        metavar='ADDRESS',
        help='Set server IP-address'
    )

    parser.add_argument(
        '-p', '--port', type=int, required=False,
        metavar='PORT',
        help='Set port'
    )

    parser.add_argument(
        '-c', '--config', type=str, required=False,
        metavar='CONFIG_FILE',
        help='Set config file'
    )

    args = parser.parse_args()

    config = {
        'server': DEFAULT_SERVER,
        'port': DEFAULT_PORT,
        'buffersize': DEFAULT_BUFFERSIZE
    }

    if args.server:
        config['server'] = args.addr

    if args.port:
        config['port'] = args.port

    if args.config:
        with open(args.config) as file:
            file_config = yaml.load(file, Loader=yaml.Loader)
            config.update(file_config)

    return config

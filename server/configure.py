from argparse import ArgumentParser
import yaml


DEFAULT_ADDR = 'localhost'
DEFAULT_PORT = 7777
DEFAULT_BUFFERSIZE = 1024


def get_config():
    parser = ArgumentParser()

    parser.add_argument(
        '-a', '--addr', type=str, required=False,
        metavar='ADDRESS',
        help='Set IP-address for listen'
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
        'addr': DEFAULT_ADDR,
        'port': DEFAULT_PORT,
        'buffersize': DEFAULT_BUFFERSIZE
    }

    if args.addr:
        config['addr'] = args.addr

    if args.port:
        config['port'] = args.port

    if args.config:
        with open(args.config) as file:
            file_config = yaml.load(file, Loader=yaml.Loader)
            config.update(file_config)

    return config

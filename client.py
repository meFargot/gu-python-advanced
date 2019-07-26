from argparse import ArgumentParser
import socket

import yaml


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
    'server': 'localhost',
    'port': 7777,
    'buffersize': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

to_msg = input('Enter message: ')
b_to_msg = to_msg.encode()


sock = socket.socket()
serv, port = config.get('server'), config.get('port')
sock.connect((serv, port))
sock.send(b_to_msg)
b_from_msg = sock.recv(config.get('buffersize'))
from_msg = b_from_msg.decode()
print(f'Server response: {from_msg}')

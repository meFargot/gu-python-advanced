from argparse import ArgumentParser
import socket

import yaml


ECHO = 'echo'

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
    'addr': 'localhost',
    'port': 7777,
    'buffersize': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

sock = socket.socket()
addr, port = config.get('addr'), config.get('port')
sock.bind((addr, port))
print(f'Server bind at {addr}:{port}')
sock.listen()
print(f'Server listen')

try:
    while True:
        client, from_address = sock.accept()
        from_ip, from_port = from_address[0], from_address[1]
        print(f'Get connection from {from_ip}:{from_port}')
        b_from_msg = client.recv(config.get('buffersize'))
        from_msg = b_from_msg.decode()
        print(f'Get message: {from_msg}')
        to_msg = ECHO
        b_to_msg = to_msg.encode()
        client.send(b_to_msg)
        print(f'Send echo response')
        client.close()
        print(f'Close connection from {from_ip}:{from_port}')

        if from_msg == 'STOP':
            exit()
except KeyboardInterrupt:
    print(f'\nServer stop')

import socket
import json
from datetime import datetime

from configure import get_config


config = get_config()

action = input('Enter action: ')
data = input('Enter data: ')

request = {
    'action': action,
    'time': datetime.now().timestamp(),
    'data': data
}

str_request = json.dumps(request)

sock = socket.socket()
serv, port = config.get('server'), config.get('port')

try:
    sock.connect((serv, port))
    print(f'Client connected to server {serv}:{port}')

    sock.send(str_request.encode())
    print(f'Client send data: {data}')

    b_response = sock.recv(config.get('buffersize'))
    response = b_response.decode()

    print(f'Server response: {response}')

except ConnectionRefusedError:
    print(f'Connection to {serv}:{port} refused')

except KeyboardInterrupt:
    print(f'Client shutdown')

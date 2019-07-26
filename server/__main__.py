import socket
import json

from configure import get_config
from protocol import validate_request, make_response


config = get_config()
addr, port = config.get('addr'), config.get('port')

try:
    sock = socket.socket()
    sock.bind((addr, port))
    sock.listen(5)
    print(f'Server started at {addr}:{port}')

    while True:
        client, from_address = sock.accept()
        from_ip, from_port = from_address[0], from_address[1]
        print(f'Get connection from {from_ip}:{from_port}')

        b_request = client.recv(config.get('buffersize'))
        request = json.loads(b_request.decode())

        if validate_request(request):
            print(f'Client send valid request: {request}')
            response = make_response(request, 200, data=request.get('data'))
        else:
            print(f'Client send invalid request: {request}')
            response = make_response(request, 404, 'Wrong request')

        str_response = json.dumps(response)
        client.send(str_response.encode())

        client.close()

        if request.get('action') == 'STOP':
            print(f'\nServer stop by client')
            exit()

except KeyboardInterrupt:
    print(f'\nServer stop')

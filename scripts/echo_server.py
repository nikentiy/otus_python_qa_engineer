import socket
import logging
from http import HTTPStatus

logging.basicConfig(level=logging.DEBUG)

HOST = "127.0.0.1"
PORT = 56785


def parse_request(data: str):
    temp = data.split('\r\n')
    method, path, protocol = [i.strip() for i in temp[0].split()]

    headers = {}
    for k, v in [i.split(':', 1) for i in temp[1:-1] if len(i) > 0]:
        headers[k.strip()] = v.strip()
    params = {}
    if '?' in path:
        str_params = path.split('?')[1]
        for k ,v in [i.split('=', 1) for i in str_params.split('&')]:
            params[k.strip()] = v.strip()
    return method, path, params, protocol, headers


def get_status(params: dict):
    status = params.get('status')
    if status:
        return f'{status} {HTTPStatus(int(status)).phrase}'
    return f'{HTTPStatus.OK} {HTTPStatus(200).phrase}'


def get_response(data: str):
    method, path, params, protocol, headers = parse_request(data)
    status = get_status(params)
    response = f"Request Method: {method}\nRequest Source: ('127.0.0.1', 47296)\n" \
               f"Response Status: {status}\n"
    for k in headers.keys():
        response.join(f"{k}: {headers.get(k)}")
    return response


with socket.socket() as server:
    server.bind((HOST, PORT))
    server.listen()
    while True:
        client_connection, client_address = server.accept()
        logging.info(f"Receiving data from {client_address}")
        data = client_connection.recv(1024).decode("utf-8")
        if not data:
            break

        logging.info(f"received data:\n{data}")
        response = get_response(data)
        client_connection.send(response.encode("utf-8"))

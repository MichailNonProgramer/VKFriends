import socket
import ssl
import re


def request(socket, request) :
    socket.send((request + '\n').encode())
    recv_data = socket.recv(65535)
    return recv_data


def qet(token: str, host: str, user_id: str):
    return \
        f"""GET /method/friends.get?user_id={user_id}&fields=nickname&access_token={token}&v=5.131 HTTP/1.1\nHost: {host}\nAccept: */*\n\n"""

token = ""
user_id = ""
host = "api.vk.com"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as api:
    api.connect((host, 443))
    api = ssl.wrap_socket(api)
    print(qet(token, host, user_id))
    req = request(api, qet(token, host, user_id))
    friends = api.recv(65535).decode()
    f = friends.split("\"")
    r = re.compile("[а-яА-Я]+")
    russian = [w for w in filter(r.match, f)]
    for i in range(0, len(russian), 2):
        print(russian[i] + " " + russian[i + 1])
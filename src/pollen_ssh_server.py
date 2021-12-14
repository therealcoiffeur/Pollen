import paramiko
import socket
import sys
import threading
import _thread


LOGFILE = "log/ssh_server.log"
LOGFILE_LOCK = threading.Lock()
HOST_KEY = paramiko.RSAKey(filename="config/ssh_server.key")


class CustomHandler(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        LOGFILE_LOCK.acquire()
        try:
            f = open(LOGFILE,"a+")
            f.write(f"{username} {password}\n")
            f.close()
        finally:
            LOGFILE_LOCK.release()
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"


def handleConnection(client):
    transport = paramiko.Transport(client)
    transport.add_server_key(HOST_KEY)
    transport.start_server(server=CustomHandler())
    channel = transport.accept(1)
    if not channel is None:
        channel.close()


def run(addr="127.0.0.1", port=65422):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((addr, port))
        server_socket.listen(100)

        print(f"Starting SSH server on {addr}:{port}")
        while(True):
            try:
                client_socket, client_addr = server_socket.accept()
                _thread.start_new_thread(handleConnection,(client_socket,))
            except Exception as e:
                print("ERROR: Client handling")
                print(e)

    except Exception as e:
        print("ERROR: Failed to create socket")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    address = "127.0.0.1"
    port = 65422
    run(addr=address, port=port)
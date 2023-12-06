import socket
import threading
import logging
from GameManager import GameManager
import json


class Server(threading.Thread):

    def __init__(self,):
        threading.Thread.__init__(self)


    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_host = '0.0.0.0'
        server_port = 8888
        server_socket.bind((server_host, server_port))
        server_socket.listen()

        logging.info(f"[Server] Server listening on {server_host}:{server_port}")

        while True:
            client_socket, address = server_socket.accept()
            logging.info(f"[Server] Accepted connection from {address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_thread.start()


    def handle_client(self, client_socket, address):
        GameManager().register_player(client_socket)
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            GameManager().data_sent_from(client_socket, data)

        client_socket.close()
        GameManager().unregister_player(client_socket)
        logging.info(f"[Server] Connection with {address} closed")
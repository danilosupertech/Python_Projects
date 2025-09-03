"""
Cliente de Chat Múltiplo (Multi-Client Chat Client)

🇧🇷 Português:
---------------
Este cliente conecta-se ao servidor de chat e:
    - Envia mensagens digitadas pelo usuário.
    - Recebe e exibe mensagens de outros clientes.

🇺🇸 English:
---------------
This client connects to the chat server and:
    - Sends messages typed by the user.
    - Receives and displays messages from other clients.

Execução | Run:
    python client.py
"""

import socket
import threading


def receive_messages(sock: socket.socket) -> None:
    """
    🇧🇷 Escuta mensagens recebidas do servidor e as exibe.
    🇺🇸 Listens for incoming messages from the server and displays them.
    """
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"\n{msg}")
            else:
                break
        except:
            print("Conexão encerrada pelo servidor | Connection closed by server")
            break


def start_client(host: str = "127.0.0.1", port: int = 5555) -> None:
    """
    🇧🇷 Inicializa o cliente de chat:
        - Conecta ao servidor.
        - Cria uma thread para ouvir mensagens.
        - Permite envio de mensagens pelo usuário.

    🇺🇸 Initializes the chat client:
        - Connects to the server.
        - Creates a thread to listen for messages.
        - Allows user to send messages.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"Conectado ao servidor | Connected to server {host}:{port}")

    thread = threading.Thread(target=receive_messages, args=(sock,))
    thread.start()

    while True:
        msg = input("> ")
        if msg.lower() in ["sair", "exit", "quit"]:
            break
        sock.send(msg.encode())

    sock.close()


if __name__ == "__main__":
    start_client()

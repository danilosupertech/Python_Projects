"""
Servidor de Chat Múltiplo (Multi-Client Chat Server)

🇧🇷 Português:
---------------
Este servidor aceita múltiplos clientes e permite que eles troquem mensagens
em tempo real. As mensagens recebidas de um cliente são retransmitidas para
todos os outros conectados.

🇺🇸 English:
---------------
This server accepts multiple clients and allows them to exchange messages
in real-time. Messages received from one client are broadcast to all others.

Execução | Run:
    python server.py
"""

import socket
import threading

# Lista global para armazenar os clientes conectados | Global list to store connected clients
clients = []


def broadcast(message: bytes, connection: socket.socket) -> None:
    """
    🇧🇷 Envia uma mensagem recebida de um cliente para todos os outros conectados,
    exceto o remetente.

    🇺🇸 Sends a message received from one client to all other connected clients,
    except the sender.
    """
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(conn: socket.socket, addr: tuple) -> None:
    """
    🇧🇷 Gerencia a comunicação com um cliente específico:
        - Recebe mensagens.
        - Exibe no servidor.
        - Envia para outros clientes.
        - Remove cliente ao desconectar.

    🇺🇸 Handles communication with a specific client:
        - Receives messages.
        - Displays them on the server.
        - Broadcasts to other clients.
        - Removes client when disconnected.
    """
    print(f"Novo cliente conectado | New client connected: {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"{addr} disse/says: {msg.decode()}")
            broadcast(msg, conn)
        except:
            break
    print(f"Cliente {addr} desconectado | Client {addr} disconnected.")
    clients.remove(conn)
    conn.close()


def start_server(host: str = "0.0.0.0", port: int = 5555) -> None:
    """
    🇧🇷 Inicializa o servidor de chat:
        - Cria socket.
        - Aceita múltiplas conexões.
        - Cria uma thread por cliente.

    🇺🇸 Initializes the chat server:
        - Creates socket.
        - Accepts multiple connections.
        - Spawns one thread per client.
    """

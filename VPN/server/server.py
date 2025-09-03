import socket

def start_server(host="0.0.0.0", port=5555):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Servidor VPN rodando em {host}:{port}")
    conn, addr = s.accept()
    print(f"Conexão recebida de {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Mensagem recebida:", data.decode())
        conn.sendall(data)
    conn.close()

if __name__ == "__main__":
    start_server()

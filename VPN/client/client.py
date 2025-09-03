import socket

def start_client(server_ip="127.0.0.1", port=5555):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))
    print(f"Conectado ao servidor VPN {server_ip}:{port}")
    while True:
        msg = input("Digite uma mensagem (ou 'sair'): ")
        if msg.lower() == 'sair':
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        print("Resposta do servidor:", data.decode())
    s.close()

if __name__ == "__main__":
    start_client()

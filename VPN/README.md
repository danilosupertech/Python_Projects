# Python VPN (conceito)

Este projeto demonstra uma **VPN simples em Python** (apenas para aprendizado).  
Inclui um cliente e servidor que simulam o tráfego encapsulado.

## Estrutura
```
python_vpn/
├── client/
│   └── client.py
├── server/
│   └── server.py
├── requirements.txt
└── README.md
```

## Como usar
1. Clone este repositório ou extraia o zip.  
2. Inicie o servidor:
   ```bash
   python server/server.py
   ```
3. Em outro terminal, inicie o cliente:
   ```bash
   python client/client.py
   ```
4. Troque mensagens entre cliente e servidor.

## Aviso
Este projeto **não é uma VPN real** para produção.  
Serve apenas como exemplo educacional usando `socket` em Python.

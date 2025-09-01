
# 📱 QR Code Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![Status](https://img.shields.io/badge/Status-Stable-success)

Um gerador de QR Codes com **interface gráfica** simples e intuitiva desenvolvido em Python com `Tkinter` e a biblioteca `qrcode`.  
Permite criar, visualizar e salvar QR Codes a partir de qualquer texto ou URL.

---

## ✨ Funcionalidades

✅ Interface gráfica amigável  
✅ Geração de QR Codes com alto nível de correção de erros  
✅ Suporte a textos, URLs, acentos e caracteres especiais  
✅ Exibição do QR Code na interface  
✅ Opção de salvar em formato PNG  
✅ Código simples, comentado e de fácil manutenção

---

## 🛠️ Tecnologias e Bibliotecas

- [Python 3.8+](https://www.python.org/) – Linguagem principal  
- [qrcode](https://pypi.org/project/qrcode/) – Geração de QR Codes  
- [Pillow](https://pypi.org/project/Pillow/) – Manipulação de imagens  
- Tkinter – Interface gráfica (vem com o Python)  
- [shutil](https://docs.python.org/3/library/shutil.html) – Para cópia e manipulação de arquivos

---

## 📥 Instalação

1. **Clone este repositório:**

```bash
git clone https://github.com/danilosupertech/qr-code-generator.git
cd qr-code-generator
```

2. **Crie um ambiente virtual (opcional):**

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. **Instale as dependências:**

```bash
pip install qrcode[pil] pillow
```

---

## ▶️ Como Executar

Rode o arquivo principal:

```bash
python qr_code_generator.py
```

- Digite o texto ou URL desejado.  
- Clique em **Generate QR Code** para gerar.  
- Clique em **Save QR Code** para salvar a imagem.  

---

## 🧪 Como Testar

Você pode testar diretamente no terminal sem abrir a interface gráfica:

```bash
python -m qrcode "https://github.com/danilosupertech" > test.png
```

Isso gera um QR Code simples salvo como `test.png`.

---

## 📂 Estrutura do Projeto

```
qr-code-generator/
├── qr_code_generator.py    # Código principal do gerador de QR Codes
├── README.md               # Documentação do projeto
└── example.png             # Exemplo de QR Code (opcional)
```

---

## 📸 Interface

![Screenshot](./example.png)

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Siga os passos:
1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Envie um Pull Request

---

👨‍💻 Desenvolvido por [Danilo SuperTech](https://github.com/danilosupertech)

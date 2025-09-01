import qrcode


def gerar_qr_code(texto, arquivo_saida="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(arquivo_saida)
    print(f"✅ QR Code gerado e salvo em {arquivo_saida}")


if __name__ == "__main__":
    texto = input("Digite o texto/URL para gerar o QR Code: ")
    gerar_qr_code(texto)

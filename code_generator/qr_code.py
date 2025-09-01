import qrcode

# Function to generate a QR Code image from text/URL
def gerar_qr_code(texto, arquivo_saida="qrcode.png"):
    """
    Generates a QR Code from the provided text or URL and saves it to a file.
    
    Parameters:
    - texto: The text or URL to encode in the QR Code.
    - arquivo_saida: Output filename for the QR Code image (default: 'qrcode.png').
    
    Note: This version does NOT use a graphical interface. It runs in the console.
    """
    qr = qrcode.QRCode(
        version=1,  # Version 1: smallest size QR code (21x21 modules)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction (~7% of codewords can be restored)
        box_size=10,  # Size of each QR code box in pixels
        border=4,     # Border thickness (minimum recommended is 4)
    )
    qr.add_data(texto)  # Add the input text/URL to the QR code
    qr.make(fit=True)   # Automatically fit the QR code to the data

    # Generate the image with black foreground and white background
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(arquivo_saida)  # Save the QR code image to the specified file
    print(f"✅ QR Code generated and saved as {arquivo_saida}")  # Inform the user

# Main entry point
if __name__ == "__main__":
    # Prompt the user to enter text/URL via console input
    texto = input("Enter the text/URL to generate the QR Code: ")
    gerar_qr_code(texto)  # Generate and save the QR code

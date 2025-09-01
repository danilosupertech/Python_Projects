import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import shutil


def generate_qr(text):
    """
    Gera um QR Code válido a partir do texto/URL fornecido.
    """
    qr = qrcode.QRCode(
        version=None,  # Ajusta automaticamente ao tamanho do texto
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    filename = 'qr_code.png'
    img.save(filename)
    return filename


def save_qr(filename):
    """
    Salva uma cópia do QR Code em local escolhido.
    """
    filepath = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG Images', '*.png')]
    )
    if filepath:
        shutil.copy(filename, filepath)
        messagebox.showinfo('QR Code Saved!', f'Saved to {filepath}')


def create_window():
    """
    Interface gráfica para gerar QR Codes.
    """
    window = tk.Tk()
    window.title('QR Code Generator')

    tk.Label(window, text='Enter the text/URL:').pack(pady=5)
    ent = tk.Entry(window, width=50)
    ent.pack(pady=5)

    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack(pady=10)

    def generate_and_display():
        text = ent.get()
        if not text.strip():
            messagebox.showwarning(
                "Input required", "Please enter some text or URL.")
            return

        filename = generate_qr(text)
        img = Image.open(filename)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        canvas.create_image(150, 150, image=photo)
        canvas.image = photo

        tk.Button(window, text='Save QR Code',
                  command=lambda: save_qr(filename)).pack(pady=5)

    tk.Button(window, text='Generate QR Code',
              command=generate_and_display).pack(pady=5)
    window.mainloop()


if __name__ == '__main__':
    create_window()

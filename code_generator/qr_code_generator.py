import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import shutil

# Function to generate a QR code image from text or URL
def generate_qr(text):
    """
    Generates a valid QR Code from the given text or URL.
    """
    qr = qrcode.QRCode(
        version=None,  # Automatically adjusts QR code size based on the text length
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Size of each QR code box in pixels
        border=4,     # Thickness of the border (minimum is 4)
    )
    qr.add_data(text)  # Add the input text/URL to the QR code
    qr.make(fit=True)  # Fit the QR code to the content

    # Create an image from the QR code
    img = qr.make_image(fill_color='black', back_color='white')
    filename = 'qr_code.png'  # Temporary file name
    img.save(filename)  # Save the QR code image
    return filename  # Return the filename for further use

# Function to save the QR code to a user-specified location
def save_qr(filename):
    """
    Saves a copy of the QR Code to a chosen location via a file dialog.
    """
    # Open a "Save As" dialog to select the file path
    filepath = filedialog.asksaveasfilename(
        defaultextension='.png',  # Ensure the file is saved as PNG
        filetypes=[('PNG Images', '*.png')]  # Limit file type to PNG
    )
    if filepath:  # Only proceed if a file path is chosen
        shutil.copy(filename, filepath)  # Copy the temporary file to the chosen path
        messagebox.showinfo('QR Code Saved!', f'Saved to {filepath}')  # Inform the user

# Function to create the main GUI window
def create_window():
    """
    Creates the main graphical interface for generating QR Codes.
    """
    window = tk.Tk()  # Initialize the main window
    window.title('QR Code Generator')  # Set the window title

    # Label prompting user input
    tk.Label(window, text='Enter the text/URL:').pack(pady=5)
    # Entry widget for user input
    ent = tk.Entry(window, width=50)
    ent.pack(pady=5)

    # Canvas widget to display the generated QR code
    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack(pady=10)

    # Inner function to handle QR code generation and display
    def generate_and_display():
        text = ent.get()  # Get text from input
        if not text.strip():  # Check if input is empty
            messagebox.showwarning(
                "Input required", "Please enter some text or URL.")  # Show warning
            return

        filename = generate_qr(text)  # Generate the QR code
        img = Image.open(filename)  # Open the generated image
        img = img.resize((300, 300), Image.Resampling.LANCZOS)  # Resize for display
        photo = ImageTk.PhotoImage(img)  # Convert to PhotoImage for Tkinter

        canvas.create_image(150, 150, image=photo)  # Display image in the center of canvas
        canvas.image = photo  # Keep a reference to prevent garbage collection

        # Button to save the QR code image
        tk.Button(window, text='Save QR Code',
                  command=lambda: save_qr(filename)).pack(pady=5)

    # Button to trigger QR code generation
    tk.Button(window, text='Generate QR Code',
              command=generate_and_display).pack(pady=5)

    window.mainloop()  # Run the Tkinter event loop

# Entry point of the program
if __name__ == '__main__':
    create_window()  # Start the GUI

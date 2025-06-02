from tkinter import filedialog
from PIL import Image
from utils import show_success

def image_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        img = Image.open(file_path).convert("RGB")
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_path:
            img.save(output_path)
            show_success("Image converted to PDF successfully.")
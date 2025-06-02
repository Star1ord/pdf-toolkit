from tkinter import filedialog
import fitz 
from utils import show_success

def compress_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_path:
            doc = fitz.open(file_path)
            doc.save(output_path, garbage=4, deflate=True, clean=True)
            doc.close()
            show_success("PDF compressed successfully.")

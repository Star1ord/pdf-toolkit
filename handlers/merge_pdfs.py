from tkinter import filedialog
from PyPDF2 import PdfMerger
from utils import show_success

def merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        merger = PdfMerger()
        for f in files:
            merger.append(f)
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_path:
            merger.write(output_path)
            merger.close()
            show_success("PDFs merged successfully.")

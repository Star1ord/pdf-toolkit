from tkinter import filedialog
from PIL import Image
import fitz
import pytesseract
from utils import show_success
from dotenv import load_dotenv
import os

load_dotenv()
TESSERACT_PATH = os.getenv("TESSERACT_PATH")

def extract_text_from_pdf():
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text += pytesseract.image_to_string(img) + "\n\n"
        output = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(text)
            show_success("Text extracted from PDF and saved.")
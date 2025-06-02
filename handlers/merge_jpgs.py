from PIL import Image
from tkinter import filedialog
from utils import show_success

def merge_jpgs():
    files = filedialog.askopenfilenames(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if files:
        images = [Image.open(f).convert("RGB") for f in files]
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_path:
            images[0].save(output_path, save_all=True, append_images=images[1:])
            show_success("Merged JPGs into PDF successfully.")
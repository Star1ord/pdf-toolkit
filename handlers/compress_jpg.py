from utils import show_success
import os
from tkinter import filedialog
from PIL import Image


def compress_jpg():
    files = filedialog.askopenfilenames(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if files:
        out_dir = filedialog.askdirectory(title="Select Output Folder")
        for f in files:
            img = Image.open(f)
            name = os.path.basename(f)
            img.save(os.path.join(out_dir, f"compressed_{name}"), "JPEG", quality=50)
        show_success(f"{len(files)} JPGs compressed and saved to selected folder.")

from tkinter import filedialog
from PIL import Image
from utils import show_success

def convert_png_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open(file_path).convert("RGB")
        output_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg;*.jpeg")]
        )
        if output_path:
            img.save(output_path, "JPEG", quality=85)
            show_success("PNG converted to JPG successfully.")
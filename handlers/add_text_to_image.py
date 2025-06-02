from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from utils import show_success

def add_text_to_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        img = Image.open(file_path)
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except:
            font = ImageFont.load_default()
        draw.text((10, 10), "Signed: Nurzhas", fill="black", font=font)
        output_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG files", "*.jpg;*.jpeg")]
        )
        if output_path:
            img.save(output_path)
            show_success("Text added and image saved.")
import tkinter as tk
from handlers import compress_jpg
from handlers import add_text_to_image
from handlers import convert_png_to_jpg
from handlers import image_to_pdf
from handlers import merge_jpgs
from handlers import merge_pdfs
from handlers import compress_pdf
from handlers import extract_text_from_pdf
from config import current_lang, languages
from utils import switch_language
from theme import toggle_night_mode

def build_tool_frames(root, components):
    # --- Title ---
    title_label = tk.Label(root, text="🧰 I ♥ PDF Toolkit", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#1a73e8")
    title_label.pack(pady=10)
    components["title_label"] = title_label

    # --- Instructions ---
    inst_frame = tk.Frame(root, bg="#e3f2fd", padx=10, pady=10, bd=1, relief="solid")
    inst_frame.pack(pady=(0, 10), padx=10, fill="x")

    instruction_label = tk.Label(
        inst_frame,
        text=languages[current_lang]['instructions'],
        justify="left",
        font=("Arial", 11, "bold"),
        bg="#e3f2fd"
    )
    instruction_label.pack(anchor="w")
    components["instruction_label"] = instruction_label
    components["inst_frame"] = inst_frame

    # --- Language Switcher ---
    lang_frame = tk.Frame(root, bg="#f0f4f8")
    lang_frame.pack(pady=5)
    components["lang_frame"] = lang_frame

    tk.Label(lang_frame, text="🌐 Language:", bg="#f0f4f8").pack(side="left")
    lang_var = tk.StringVar(value=current_lang)
    lang_menu = tk.OptionMenu(lang_frame, lang_var, *languages.keys(),
                              command=lambda lang: switch_language(lang, components, languages))
    lang_menu.pack(side="left")

    # --- Night Mode Toggle ---
    misc_frame = tk.Frame(root, bg="#f0f4f8")
    misc_frame.pack(pady=10)
    toggle_btn = tk.Button(
        misc_frame,
        text="🌓 Toggle Night Mode",
        command=lambda: toggle_night_mode(components["root"], components),
        bg="#d1c4e9",
        font=("Arial", 10)
    )
    toggle_btn.pack()
    components["misc_frame"] = misc_frame

    # --- Image Tools Section ---
    img_frame = tk.LabelFrame(root, text="🖼 Image Tools", font=("Arial", 12, "bold"),
                              bg="#ffffff", fg="#444", padx=10, pady=10)
    img_frame.pack(padx=20, pady=10, fill="both")
    components["img_frame"] = img_frame

    btn_compress_jpg = tk.Button(img_frame, text="📉 Compress JPGs", command=compress_jpg, width=30, bg="#e8f0fe")
    btn_compress_jpg.pack(pady=4)
    components["btn_compress_jpg"] = btn_compress_jpg

    btn_add_text = tk.Button(img_frame, text="🖊 Add Text to Image", command=add_text_to_image, width=30, bg="#e8f0fe")
    btn_add_text.pack(pady=4)
    components["btn_add_text"] = btn_add_text

    btn_png_to_jpg = tk.Button(img_frame, text="🌈 Convert PNG to JPG", command=convert_png_to_jpg, width=30, bg="#e8f0fe")
    btn_png_to_jpg.pack(pady=4)
    components["btn_png_to_jpg"] = btn_png_to_jpg

    btn_img_to_pdf = tk.Button(img_frame, text="🧾 Convert Image to PDF", command=image_to_pdf, width=30, bg="#e8f0fe")
    btn_img_to_pdf.pack(pady=4)
    components["btn_img_to_pdf"] = btn_img_to_pdf

    # --- PDF Tools Section ---
    pdf_frame = tk.LabelFrame(root, text="📄 PDF Tools", font=("Arial", 12, "bold"),
                              bg="#ffffff", fg="#444", padx=10, pady=10)
    pdf_frame.pack(padx=20, pady=10, fill="both")
    components["pdf_frame"] = pdf_frame

    btn_merge_jpg_pdf = tk.Button(pdf_frame, text="📂 Merge JPGs into PDF", command=merge_jpgs, width=30, bg="#fce8e6")
    btn_merge_jpg_pdf.pack(pady=4)
    components["btn_merge_jpg_pdf"] = btn_merge_jpg_pdf

    btn_merge_pdfs = tk.Button(pdf_frame, text="📂 Merge PDFs", command=merge_pdfs, width=30, bg="#fce8e6")
    btn_merge_pdfs.pack(pady=4)
    components["btn_merge_pdfs"] = btn_merge_pdfs

    btn_compress_pdf = tk.Button(pdf_frame, text="🗜 Compress PDF", command=compress_pdf, width=30, bg="#fce8e6")
    btn_compress_pdf.pack(pady=4)
    components["btn_compress_pdf"] = btn_compress_pdf

    btn_ocr_pdf = tk.Button(pdf_frame, text="🧾 OCR Extract from PDF", command=extract_text_from_pdf, width=30, bg="#fce8e6")
    btn_ocr_pdf.pack(pady=4)
    components["btn_ocr_pdf"] = btn_ocr_pdf

    # --- Status Label ---
    status_label = tk.Label(root, text="", bg="#f0f4f8", fg="green", font=("Arial", 10))
    status_label.pack(pady=10)
    components["status_label"] = status_label
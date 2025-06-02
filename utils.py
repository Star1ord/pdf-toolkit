from tkinter import messagebox
from datetime import datetime

def show_success(msg, status_label=None):
    messagebox.showinfo("Success", msg)
    log_action(msg)
    if status_label:
        status_label.config(text=f"\u2705 {msg}")

def log_action(action):
    with open("action_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {action}\n")

def on_drop(event):
    dropped_files = event.widget.tk.splitlist(event.data)
    messagebox.showinfo("Dropped Files", "\n".join(dropped_files))


def switch_language(lang_code, components, languages):
    if "current_lang" not in components:
        components["current_lang"] = [lang_code]
    else:
        components["current_lang"][0] = lang_code
    
    # Update instruction text
    components["instruction_label"].config(text=languages[lang_code]["instructions"])
    # Update window title
    components["root"].title(languages[lang_code]["title"])

    labels = languages[lang_code]["buttons"]
    components["btn_compress_jpg"].config(text=labels["compress_jpg"])
    components["btn_add_text"].config(text=labels["add_text"])
    components["btn_png_to_jpg"].config(text=labels["png_to_jpg"])
    components["btn_img_to_pdf"].config(text=labels["img_to_pdf"])
    components["btn_merge_jpg_pdf"].config(text=labels["merge_jpg_pdf"])
    components["btn_merge_pdfs"].config(text=labels["merge_pdfs"])
    components["btn_compress_pdf"].config(text=labels["compress_pdf"])
    components["btn_ocr_pdf"].config(text=labels["ocr_pdf"])
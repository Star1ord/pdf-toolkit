import json
import os

settings_file = "settings.json"
current_lang = "EN"


def import_settings():
    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            return json.load(f)
    return {}

def export_settings(data):
    with open(settings_file, "w") as f:
        json.dump(data, f)

settings = import_settings()

languages = {
    "EN": {
        "title": "I ♥ PDF Toolkit",
        "instructions": "📌 Instructions:\n• Select a tool below.\n• Choose input file(s).\n• Choose where to save your result.",
        "buttons": {
            "compress_jpg": "📦 Batch Compress JPGs",
            "add_text": "🖊 Add Text to Image",
            "png_to_jpg": "🌈 Convert PNG to JPG",
            "img_to_pdf": "🧾 Convert Image to PDF",
            "merge_jpg_pdf": "📂 Merge JPGs into PDF",
            "merge_pdfs": "📂 Merge PDFs",
            "compress_pdf": "🗜 Compress PDF",
            "ocr_pdf": "🧾 OCR Extract from PDF",
        }
    },
    "RU": {
        "title": "Я ♥ PDF Инструменты",
        "instructions": "📌 Инструкция:\n• Выберите инструмент ниже.\n• Выберите входной файл(ы).\n• Сохраните результат.",
        "buttons": {
            "compress_jpg": "📉 Сжать JPG",
            "add_text": "🖊 Добавить текст на изображение",
            "png_to_jpg": "🌈 PNG в JPG",
            "img_to_pdf": "🧾 Картинку в PDF",
            "merge_jpg_pdf": "📂 JPG в PDF",
            "merge_pdfs": "📂 Объединить PDF",
            "compress_pdf": "🗜 Сжать PDF",
            "ocr_pdf": "🧾 OCR: Извлечь текст из PDF"
        }
    },
    "KZ": {
        "title": "Мен PDF Құралдарды ♥",
        "instructions": "📌 Нұсқаулық:\n• Құралды таңдаңыз.\n• Файл(дарды) таңдаңыз.\n• Нәтижені сақтаңыз.",
        "buttons": {
        "compress_jpg": "📉 JPG-ны қысу",
            "add_text": "🖊 Мәтінді қосу",
            "png_to_jpg": "🌈 PNG-ні JPG-ке көшіру",
            "img_to_pdf": "🧾 Суретті PDF-ке айналдыру",
            "merge_jpg_pdf": "📂 JPG-терді PDF-ке біріктіру",
            "merge_pdfs": "📂 PDF-терді біріктіру",
            "compress_pdf": "🗜 PDF-ты қысу",
            "ocr_pdf": "🧾 OCR: PDF-тен мәтінді шығару"
            }
        }
    }
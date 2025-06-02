# 🧰 I ♥ PDF Toolkit

A colorful, beginner-friendly **PDF and image utility desktop app** built using **Python** and **Tkinter**. It includes essential tools like image compression, PDF merging, OCR text extraction, language switching, night mode, and drag-and-drop support — all in a single desktop application.

## 🚀 Features

### 🖼️ Image Tools
- 📉 Compress JPGs (single & batch)
- 🖊 Add Text to Images
- 🌈 Convert PNG to JPG
- 🧾 Convert Images to PDF

### 📄 PDF Tools
- 📂 Merge JPGs into a single PDF
- 📂 Merge multiple PDF files
- 🗜 Compress PDF files
- 🔍 OCR Text Extraction from PDFs (using Tesseract)

### 🧩 Extras
- 🌗 Night Mode toggle
- 🌐 Language Switcher (Kazakh, Russian, English)
- 🖱️ Drag & Drop support for files
- 📝 Action Logging
- 🎨 Clean, colorful GUI layout

## 🛠 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Star1ord/pdf-toolkit.git
cd pdf-toolkit
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

## 🔍 Tesseract OCR Setup

### Windows
1. Download from the official repo:
   https://github.com/tesseract-ocr/tesseract/releases
2. Install and note the path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe)
3. Add to PATH or create `.env` file:
   ```ini
   TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
   ```

### macOS
```bash
brew install tesseract
```

### Linux
```bash
sudo apt update
sudo apt install tesseract-ocr
```

## ▶️ Running the App
```bash
python main.py
```

## 📁 Project Structure
```
pdf-toolkit/
├── handlers/
│ ├── init.py
│ ├── add_text_to_image.py
│ ├── compress_jpg.py
│ ├── compress_pdf.py
│ ├── convert_png_to_jpg.py
│ ├── extract_text_from_pdf.py
│ ├── image_to_pdf.py
│ ├── merge_jpgs.py
│ ├── merge_pdfs.py
├── main.py           # Application entry point
├── ui.py            # UI components
├── utils.py         # Utility functions
├── theme.py         # Theme management
├── config.py        # Configuration
├── .env            # Environment variables
├── action_log.txt  # Activity logging(appears after completing one of the features)
├── requirements.txt # Dependencies
└── README.md       # Documentation
```

## 🧪 Tested With
✅ Python 3.10+

✅ Windows 10/11

⚠️ macOS / Linux (functional, but drag-and-drop may vary)

## 📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

## 🙌 Acknowledgements
- pytesseract
- Pillow (PIL)
- TkinterDnD2
- ChatGPT for assistance
- Inspired by ILovePDF

## 🧭 Future Plans
- 🔐 PDF password protection
- 📥 Save/load task presets
- 🔄 Reordering PDF pages
- 🔧 Adjustable compression settings

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 💬 Contact
Made with 💙 by Star1ord  
Feel free to reach out via GitHub or email if you have suggestions or improvements!
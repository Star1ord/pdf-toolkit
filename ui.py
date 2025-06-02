
img_frame = tk.LabelFrame(root, text="🖼 Image Tools", font=("Arial", 12, "bold"), bg="#ffffff", fg="#444", padx=10, pady=10)
img_frame.pack(padx=20, pady=10, fill="both")

# --- Image Buttons ---
btn_compress_jpg = tk.Button(img_frame, text="📉 Compress JPGs", command=compress_jpg, width=30, bg="#e8f0fe")
btn_compress_jpg.pack(pady=4)

btn_add_text = tk.Button(img_frame, text="🖊 Add Text to Image", command=add_text_to_image, width=30, bg="#e8f0fe")
btn_add_text.pack(pady=4)

btn_png_to_jpg = tk.Button(img_frame, text="🌈 Convert PNG to JPG", command=convert_png_to_jpg, width=30, bg="#e8f0fe")
btn_png_to_jpg.pack(pady=4)

btn_img_to_pdf = tk.Button(img_frame, text="🧾 Convert Image to PDF", command=image_to_pdf, width=30, bg="#e8f0fe")
btn_img_to_pdf.pack(pady=4)

# --- Category Section - PDF ---
pdf_frame = tk.LabelFrame(root, text="📄 PDF Tools", font=("Arial", 12, "bold"), bg="#ffffff", fg="#444", padx=10, pady=10)
pdf_frame.pack(padx=20, pady=10, fill="both")

# --- PDF Buttons ---
btn_merge_jpg_pdf = tk.Button(pdf_frame, text="📂 Merge JPGs into PDF", command=merge_jpgs, width=30, bg="#fce8e6")
btn_merge_jpg_pdf.pack(pady=4)

btn_merge_pdfs = tk.Button(pdf_frame, text="📂 Merge PDFs", command=merge_pdfs, width=30, bg="#fce8e6")
btn_merge_pdfs.pack(pady=4)

btn_compress_pdf = tk.Button(pdf_frame, text="🗜 Compress PDF", command=compress_pdf, width=30, bg="#fce8e6")
btn_compress_pdf.pack(pady=4)

btn_ocr_pdf = tk.Button(pdf_frame, text="🧾 OCR Extract from PDF", command=extract_text_from_pdf, width=30, bg="#fce8e6")
btn_ocr_pdf.pack(pady=4)

# Status Label
status_label = tk.Label(root, text="", bg="#f0f4f8", fg="green", font=("Arial", 10))
status_label.pack(pady=10)
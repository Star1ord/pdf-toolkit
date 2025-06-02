def toggle_night_mode(components):
    root = components["root"]
    title_label = components["title_label"]
    instruction_label = components["instruction_label"]
    status_label = components["status_label"]
    inst_frame = components["inst_frame"]
    img_frame = components["img_frame"]
    pdf_frame = components["pdf_frame"]
    lang_frame = components["lang_frame"]
    misc_frame = components["misc_frame"]
    
    current_bg = root["bg"]
    dark_mode = "#2b2b2b"
    light_mode = "#f0f4f8"

    new_bg = dark_mode if current_bg == light_mode else light_mode
    fg = "#ffffff" if new_bg == dark_mode else "#000000"
    box_bg = "#3a3a3a" if new_bg == dark_mode else "#ffffff"
    btn_bg_img = "#44475a" if new_bg == dark_mode else "#e8f0fe"
    btn_bg_pdf = "#4c3b4d" if new_bg == dark_mode else "#fce8e6"
    inst_bg = "#404040" if new_bg == dark_mode else "#e3f2fd"


    
    root.configure(bg=new_bg)
    title_label.configure(bg=new_bg, fg="#1a73e8" if new_bg == light_mode else "#80caff")
    status_label.configure(bg=new_bg, fg=fg)
    instruction_label.configure(bg=inst_bg, fg=fg)
    inst_frame.configure(bg=inst_bg)

    # Update title and instruction heading colors
    title_label.configure(bg=new_bg, fg="#1a73e8" if new_bg == light_mode else "#80caff")
    
    # Update section label fonts (Image Tools, PDF Tools)
    img_frame.configure(fg=fg)
    pdf_frame.configure(fg=fg)
    
    # Update all frames
    for frame in [img_frame, pdf_frame, lang_frame, misc_frame]:
        frame.configure(bg=new_bg)

    # Update all children widgets (buttons, labels inside frames)
    for widget in img_frame.winfo_children():
        widget.configure(bg=btn_bg_img, fg=fg)

    for widget in pdf_frame.winfo_children():
        widget.configure(bg=btn_bg_pdf, fg=fg)

    for widget in lang_frame.winfo_children():
        widget.configure(bg=new_bg, fg=fg)

    for widget in misc_frame.winfo_children():
        widget.configure(bg="#b39ddb" if new_bg == dark_mode else "#d1c4e9", fg="#000" if new_bg == light_mode else "#fff")
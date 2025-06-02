from tkinterdnd2 import TkinterDnD, DND_FILES
import tkinter as tk
from ui import build_tool_frames
from utils import on_drop
from config import languages, current_lang


def main():
    # Root Window Setup
    root = TkinterDnD.Tk()
    root.title(languages[current_lang]["title"])
    root.geometry("600x820")
    root.config(bg="#f0f4f8")
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", on_drop)

    # Shared component registry
    components = {
        "root": root,
        "current_lang": [current_lang]  # Using list for mutability
    }

    # Build UI and register components
    build_tool_frames(root, components)

    # Start the app
    root.mainloop()

if __name__ == "__main__":
    main()
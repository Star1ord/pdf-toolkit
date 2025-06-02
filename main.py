from tkinterdnd2 import TkinterDnD
from ui import build_ui

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    build_ui(root)
    root.mainloop()
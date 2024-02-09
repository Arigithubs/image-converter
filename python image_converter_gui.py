import tkinter as tk
from tkinterdnd2 import DND_FILES
from PIL import Image
import os

def convert_image(image_path, output_format='png', quality=100):
    # Image conversion logic
    try:
        img = Image.open(image_path)
        output_name = os.path.splitext(image_path)[0] + '.' + output_format
        img.save(output_name, quality=quality)
    except Exception as e:
        print(f"Error converting file {image_path}: {e}")

def on_drop(event):
    files = root.tk.splitlist(event.data)
    for f in files:
        # Assuming the user wants PNG format and quality of 90
        convert_image(f, 'png', 90)

root = tk.Tk()
root.title("Image Converter")

# Styling the window
root.geometry("400x300")
root.configure(bg="#f2f2f2")

drop_area = tk.Label(root, text="Drag and Drop Images Here", font=("Arial", 16), bg="#ffffff", fg="#333333", relief=tk.RAISED)
drop_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

root.mainloop()

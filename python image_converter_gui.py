import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_image(image_path, output_format='png'):
    img = Image.open(image_path)
    output_name = os.path.splitext(image_path)[0] + '.' + output_format
    img.save(output_name)

def on_drop(event):
    file_path = event.data.strip()
    convert_image(file_path)  # You can specify a different format here

root = tk.Tk()
root.title('Image Converter')
root.geometry('400x200')

drop_area = tk.Label(root, text="Drag and Drop Image Here")
drop_area.pack(expand=True, fill=tk.BOTH)
drop_area.bind("<Drop>", on_drop)

root.mainloop()

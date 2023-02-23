# python3
# to get started:
# brew install libjpeg libtiff little-cms2 openjpeg webp
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow --no-binary :all:

import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import Image, ImageDraw, ImageFont
import os

# Constants for the dialog box
PINK = "#e2979c"
FONT_NAME = "Courier"

path = ''


# Get file path of the original image
def get_file():
    global path
    file = filedialog.askopenfile()
    path = os.path.abspath(file.name)
    showinfo(message=f'Selected File: {path}')


# Get font size and text from the dialog boxes
def get_parameters():
    font_size = int(font_size_box.get("1.0", 'end-1c'))
    text = text_box.get("1.0", 'end-1c')
    add_watermark(font_size, text)


# Add watermark using PIL
def add_watermark(font_size, text):
    with Image.open(path, "r") as im:
        font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", font_size)
        draw = ImageDraw.Draw(im)
        draw.text((im.size[0]/2, im.size[1]/2), text, fill="black", anchor="ms", font=font)

        im.show()
        file, ext = os.path.splitext(path)
        im.save(file + ".watermarked.jpg", "JPEG")


window = tk.Tk()
window.title("Watermarked")
window.config(pady=50, padx=50)

name_label = tk.Label(text="Add your watermark", font=(FONT_NAME, 50, "bold"), fg=PINK)
name_label.grid(column=0, row=0, columnspan=2, pady=10)

path_label = tk.Label(text="Path to the file:", font=(FONT_NAME, 20, "bold"), fg=PINK)
path_label.grid(column=0, row=1, pady=10)

path_box = tk.Button(text="Select path to the file", font=(FONT_NAME, 15), padx=3, pady=3, command=get_file)
path_box.grid(column=1, row=1, pady=10)

font_size_label = tk.Label(text="Font size:", font=(FONT_NAME, 20, "bold"), fg=PINK)
font_size_label.grid(column=0, row=2, pady=10)

font_size_box = tk.Text(height=1, width=50)
font_size_box.grid(column=1, row=2, pady=10)

text_label = tk.Label(text="Watermark text:", font=(FONT_NAME, 20, "bold"), fg=PINK)
text_label.grid(column=0, row=3, pady=10)

text_box = tk.Text(height=1, width=50)
text_box.grid(column=1, row=3, pady=10)

add_watermark_button = tk.Button(text="Generate watermarked image", font=(FONT_NAME, 20), padx=3, pady=3,
                                 command=get_parameters)
add_watermark_button.grid(column=0, row=4, columnspan=2, pady=10)

window.mainloop()

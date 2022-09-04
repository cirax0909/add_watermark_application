from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# -----------------Button function-------------------#
main_photo_directory = ""
watermark_photo_directory = ""
new_photo = ""


def browseMain():
    file = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Image files", "*.jpg*"),
                                                                                        ("all files", "*.*")))
    globals()['main_photo_directory'] = file


def browseWatermark():
    file = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Image files", "*.jpg*"),
                                                                                        ("all files", "*.*")))
    globals()['watermark_photo_directory'] = file


def watermark_with_transparency():
    base_image = Image.open(f"{main_photo_directory}").convert('RGBA')
    watermark = Image.open(f"{watermark_photo_directory}").convert('RGBA')
    watermask = watermark.convert("L").point(lambda x: min(x, 65))
    watermark.putalpha(watermask)
    new_photo = Image.new('RGBA', base_image.size, (0, 0, 0, 0))
    new_photo.paste(base_image, (0, 0))
    new_photo.paste(watermark, (0, 0), mask=watermark)
    new_photo.show()
    globals()['new_photo'] = new_photo


def save_file():
    new_image = filedialog.asksaveasfilename(initialdir="new_image", title="Select file", defaultextension=".png",
                                             filetypes=(('PNG', '*.png'), ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')),
                                                        ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
    if new_image:
        x = window.winfo_rootx()
        y = window.winfo_rooty()
        new_photo.save(new_image)


# --------------UI--------------------#
window = tk.Tk()
window.title("Watermark Creator")
window.config(padx=30, pady=20)

new_image_button = Button(text="New Image", command=browseMain)
new_image_button.grid(column=0, row=1)

new_image_button = Button(text="New Watermark", command=browseWatermark)
new_image_button.grid(column=1, row=1)

start_button = Button(text="Add Watermark", command=watermark_with_transparency)
start_button.grid(column=2, row=1)

save_image_button = Button(text="Save Image", command=save_file)
save_image_button.grid(column=3, row=1)

img = Image.open(r'E:\add_watermark_application\image\river.jpg')
width, height = img.size

canvas = tk.Canvas(window, width=800, height=560)
canvas.grid(row=2, columnspan=4, pady=20)

photo = ImageTk.PhotoImage(img)
canvas.create_image(width // 3, height // 3, image=photo)

window.mainloop()

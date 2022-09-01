from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageDraw, ImageFont, ImageTk

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
    base_image = Image.open(f"{main_photo_directory}")
    watermark = Image.open(f"{watermark_photo_directory}")
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, (0, 0), watermark)
    transparent.show()


def save_file():
    new_image = filedialog.asksaveasfile(initialfile='new_photo', defaultextension=".jpg",
                                         filetypes=[("All Files", "*.*"), ("new-image", "*.jpg")])
    if not new_image:
        return
    new_photo.save(new_image)


# --------------UI--------------------#
window = tk.Tk()
window.geometry("750x250")
window.title("Watermark Creator")
window.config(padx=30, pady=20)

new_image_button = Button(text="New Image", command=browseMain)
new_image_button.grid(column=0, row=1)

new_image_button = Button(text="New Watermark", command=browseWatermark)
new_image_button.grid(column=1, row=1)

start_button = Button(text="Add Watermark", command=watermark_with_transparency)
start_button.grid(column=2, row=1)

save_image_button = Button(text="Save Image", command=lambda: save_file())
save_image_button.grid(column=3, row=1)

img = Image.open(r'E:\add_watermark_application\image\river.jpg')
width, height = img.size

canvas = tk.Canvas(window, width=800, height=600)
canvas.grid(row=2, columnspan=4, pady=20)

photo = ImageTk.PhotoImage(img)
canvas.create_image(width // 3, height // 3, image=photo)

window.mainloop()

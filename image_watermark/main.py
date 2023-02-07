import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk


class WaterMarking:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermark your Image")
        self.master.geometry("800x800")

        self.label = tk.Label(self.master, text="Welcome to Image WaterMark")
        self.label.pack()

        self.upload_button = tk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        tk.Label(self.master, text="Text:").pack(pady=20)
        self.text_entry = tk.Entry(self.master)
        self.text_entry.pack()

        tk.Label(self.master, text="Color (Hex Code):").pack(pady=20)
        self.color_entry = tk.Entry(self.master)
        self.color_entry.pack()

        tk.Label(self.master, text="Font Size:").pack(pady=20)
        self.font_size_entry = tk.Entry(self.master)
        self.font_size_entry.pack()

        self.add_text_button = tk.Button(self.master, text="Add Text", command=self.add_text)
        self.add_text_button.pack()

        self.add_logo_button = tk.Button(self.master, text="Add Logo", command=self.add_logo)
        self.add_logo_button.pack()

        self.save_button = tk.Button(self.master, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=5)

        self.original_image = None
        self.image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        self.original_image = Image.open(file_path)
        self.original_image = self.original_image.resize((400, 400), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.original_image)
        self.label.config(image=self.image)
        self.label.image = self.image

    def add_text(self):
        text = self.text_entry.get()
        font_size = int(self.font_size_entry.get())
        font = ImageFont.truetype("/Library/Fonts/Arial.ttf", size=font_size)
        draw = ImageDraw.Draw(self.original_image)
        text_width, text_height = draw.textsize(text, font)
        # calculate the x,y position for the text
        # draw watermark in the bottom right corner
        margin = self.original_image.width * 0.1
        x = (self.original_image.width - text_width - margin)
        y = (self.original_image.height - text_height - margin)
        # add the text on the image
        draw.text((x, y), text, font=font, fill=(255, 0, 0))
        self.image = ImageTk.PhotoImage(self.original_image)
        self.label.config(image=self.image)
        self.label.image = self.image

    def add_logo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            logo = Image.open(file_path)
            logo = logo.convert("RGBA")
            # Increase size for higher resolution
            original_width, original_height = logo.size
            logo = logo.resize((int(original_width * 1.5), int(original_height * 1.5)), resample=Image.BICUBIC)
            # Converting to thumbnail
            logo.thumbnail((500, 100))
            x, y = self.original_image.size
            x, y = x - logo.size[0], y - logo.size[1]
            self.original_image.paste(logo, (x, y), logo)
            self.image = ImageTk.PhotoImage(self.original_image)
            self.label.config(image=self.image)
            self.label.image = self.image

    # def add_logo(self):
    #     file_path = filedialog.askopenfilename()
    #     if file_path:
    #         logo = Image.open(file_path)
    #         logo.thumbnail((500, 100))
    #         x, y = self.original_image.size
    #         x, y = x - logo.size[0], y - logo.size[1]
    #         self.original_image.paste(logo, (x, y))
    #         self.image = ImageTk.PhotoImage(self.original_image)
    #         self.label.config(image=self.image)
    #         self.label.image = self.image

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.label.image = self.original_image
            self.label.image.save(file_path)
            messagebox.showinfo("Info", "Image saved successfully")


root = tk.Tk()
app = WaterMarking(root)
root.mainloop()

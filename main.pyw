import customtkinter as ctk
from PIL import Image, ImageTk
import os

class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x550")
        self.title("Swoxy Calculator")

        icon_path = os.path.join(os.getcwd(), "image", "app.ico")
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        bg_image_path = os.path.join(os.getcwd(), "background", "background.jpg")
        if os.path.exists(bg_image_path):
            bg_image = Image.open(bg_image_path)
            bg_image = bg_image.resize((450, 550))
            self.bg_image_tk = ImageTk.PhotoImage(bg_image)
            bg_label = ctk.CTkLabel(self, image=self.bg_image_tk, text="") 
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=1, uniform="a")

        self.text = ctk.CTkEntry(self, width=400, height=80, font=("Space Mono", 30), justify="left")
        self.text.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10))  

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('/', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                ctk.CTkButton(self, text=text, width=80, height=80, corner_radius=5, command=self.sum).grid(row=row, column=col, padx=5, pady=5)
            else:
                ctk.CTkButton(self, text=text, width=80, height=80, corner_radius=5, command=lambda t=text: self.add(t)).grid(row=row, column=col, padx=5, pady=5)

        ctk.CTkButton(self, text="C", width=80, height=80, corner_radius=5, command=lambda: self.text.delete(0, ctk.END)).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def add(self, num: str):
        self.text.insert(ctk.END, num)

    def sum(self):
        text = self.text.get()
        try:
            total = str(eval(text))
            self.text.delete(0, ctk.END)
            self.text.insert(ctk.END, total)
        except Exception as e:
            self.text.delete(0, ctk.END)
            self.text.insert(ctk.END, "Error")
            print(f"Hata: {e}")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = Gui()
    app.mainloop()

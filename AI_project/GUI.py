import tkinter as tk
import PIL.ImageTk
import cv2 as cv
from tkinter import Label, Canvas, Button, filedialog
from PIL import Image, ImageTk
import detect

class Windows:
    def __init__(self, root):
        self.title = Label(root, text='TRAFFIC SIGN RECOGNITION', font=('Arial', 14), anchor=tk.NW, pady=10)
        self.title.pack(side=tk.TOP)
        self.canvas = Canvas(root, width= 750, height= 500)
        self.canvas.pack()
        self.frame = self.canvas.create_image(10,10, anchor=tk.NW)
        self.btn = Button(root, text='Choose file', command=lambda: self.btnHandler())
        self.btn.pack(side=tk.BOTTOM, pady=10)

    def btnHandler(self):
        img = cv.imread(filedialog.askopenfilename())
        if img is not None:
            img = detect.classificate(img)
            img = cv.resize(img, dsize=(730, 480))
            self.photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
            self.canvas.itemconfig(self.frame, image=self.photo)

root = tk.Tk()
window = Windows(root)
root.mainloop()
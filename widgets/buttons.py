import tkinter as tk


def createButton(ttk, _text, _image, function):
    btn_organizer = ttk.Button(
        text=_text,
        image=tk.PhotoImage(file=_image).subsample(1),
        compound='left',
        cursor="hand2",
        command=function)
    btn_organizer.pack(fill='both', expand=True, ipady=20)


def chageOnHover(button, imageHover, imageLeave):
    button.bind('<Enter>', func=lambda e: button.configure(
        image=imageHover))
    button.bind("<Leave>", func=lambda e: button.configure(
        image=imageLeave))

# chageOnHover(btn_organizer, folder_img, folders_img)

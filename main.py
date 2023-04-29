import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.ttk as ttk
from organizer import organizer
from setting.app import createUI
from widgets.buttons import createButton
from tkinter.simpledialog import askstring
from makeproject import makeVoidProject

# Execute for HD windows, compatible with S.O windows
try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass


# def newProject():
#     new_window = tk.Toplevel(app)
#     new_window.overrideredirect(1)
#     app.tk.eval(f'tk::PlaceWindow {str(new_window)} center')
#     btn_web = ttk.Button(new_window, image=web_project_void_img,
#                          command=lambda: new_window.destroy())
#     btn_web.grid(row=1, column=0)
#     def name_project(): return askstring(new_window, "Nombre para el proyecto nuevo")
#     btn_project_web = ttk.Button(new_window,
#                                  image=web_project_void_img,
#                                  text="Proyecto web vacio",
#                                  command=lambda: makeVoidProject(getDirectory(), name_project()))
#     btn_project_web.grid(row=1, column=1)
#     chageOnHover(btn_project_web, web_project_void_hover_img,
#                  web_project_void_img)
#     return new_window


def organizar():
    organizer(askdirectory())


if __name__ == "__main__":
    app = createUI(tk.Tk(), ttk.Style())
    createButton(ttk, "Organizar", './assets/kawaii_folder.png',
                 organizar)

    app.mainloop()

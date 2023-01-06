import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import tkinter.filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up Initial Things
        self.title("OSU Manager")
        self.geometry("720x550")
        self.resizable(True, True)
        # self.iconphoto(False, tk.PhotoImage(file="assets/title_icon.png"))

        # Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create Menubar of the app
        self.menubar = Menubar(self).menubar

        # Initialize Frames
        self.frames = {}
        for F in {HomePage, Download}:  # HACK: Don't add here the frames
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        self.configure(menu=self.menubar)  # Pass the menubar to app configuration
        frame.tkraise()  # This line will put the frame on front


# ------------------------------------------------- MENU BAR ----------------------------------------------------------------------------------


class Menubar:
    def __init__(self, parent):
        self.create_menubar(parent)
        parent.config(menu=self.menubar)

    def create_menubar(self, parent):
        self.menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Applicationmenu
        applicationmenu = Menu(
            self.menubar, tearoff=0, relief=RAISED, activebackground="#026AA9"
        )
        applicationmenu.add_command(
            label="Home", command=lambda: parent.show_frame(HomePage)
        )
        self.menubar.add_cascade(label="Application", menu=applicationmenu)
        applicationmenu.add_command(
            label="Download Beatmaps", command=lambda: parent.show_frame(Download)
        )
        applicationmenu.add_separator()
        applicationmenu.add_command(label="Exit", command=parent.quit)

        # configuration menu
        config_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Configuration", menu=config_menu)
        config_menu.add_command(label="User", command=lambda: self.set_user(parent))
        config_menu.add_command(
            label="Local Beatmaps", command=lambda: self.set_localpath(parent)
        )
        # config_menu.add_separator()

        # help menu
        help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)
        # help_menu.add_separator()

    def set_localpath(self, parent):
        localpath = tkinter.filedialog.askdirectory()
        if localpath is not None:
            print(f"Folder path: {localpath}")  # TODO: Do something with the user input

    def set_user(self, parent):
        user = tkinter.simpledialog.askstring(
            "User", "Enter your OSU! player name or code:"
        )
        if user is not None:
            print(f"User input: {user}")  # TODO: Do something with the user input

    def about(self):
        messagebox.showinfo("About", "This is a sample Application")


# ---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------


class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Home Page", font=("Times", "20"))
        label.pack(pady=0, padx=0)

        # ADD CODE HERE TO DESIGN THIS PAGE


# ---------------------------------------- Download Beatmaps FRAME / CONTAINER ------------------------------------------------------------------


class Download(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Download Beatmaps", font=("Times", "20"))
        label.pack(pady=0, padx=0)

        # ADD CODE HERE TO DESIGN THIS PAGE


if __name__ == "__main__":
    app = App()
    app.mainloop()

    # IF you find this useful >> Claps on Medium >> Stars on Github >> Subscription on youtube will help me

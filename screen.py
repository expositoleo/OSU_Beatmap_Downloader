import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MainMenu(tk.Frame):
    def __init__(self):
        "Screen with buttons goes here"
        self.inputs = "inputs"
        self.data_path = "/path"

    def send_input(slef, input):
        self.persistence = Persistence(data_path)
        self.expert = Expert(self.inputs, self.persistence, self)


if __name__ == "__main__":

    # Create the main window
    window = tk.Tk()
    window.title("OSU! Beatmap Downloader")

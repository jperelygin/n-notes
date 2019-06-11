#!/usr/bin/python3
import tkinter as tk

class Reminder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_reminder()

    def create_reminder(self):
        self.button = tk.Button(self)
        self.button["text"] = "Have you made a note?"
        self.button["command"] = self.master.destroy
        self.button.pack(side="top")

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_geometry("300x200")
    root.title("NOTE!")
    app = Reminder(master=root)
    app.mainloop()

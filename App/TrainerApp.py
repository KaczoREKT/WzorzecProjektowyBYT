import tkinter as tk
from tkinter import messagebox

class TrainerApp:
    def __init__(self, lekcja):
        self.lekcja = lekcja
        self.window = tk.Tk()
        self.window.title("Panel Trenera")

        tk.Label(self.window, text="Data:").pack()
        self.data_entry = tk.Entry(self.window)
        self.data_entry.pack()

        tk.Label(self.window, text="Godzina rozpoczęcia:").pack()
        self.start_time_entry = tk.Entry(self.window)
        self.start_time_entry.pack()

        tk.Label(self.window, text="Godzina zakończenia:").pack()
        self.end_time_entry = tk.Entry(self.window)
        self.end_time_entry.pack()

        tk.Button(self.window, text="Dodaj Lekcję", command=self.add_lesson).pack()

    def add_lesson(self):
        data = {
            "data": self.data_entry.get(),
            "start_time": self.start_time_entry.get(),
            "end_time": self.end_time_entry.get()
        }
        self.lekcja.add_lesson(data)
        messagebox.showinfo("Sukces", "Lekcja została dodana!")

    def run(self):
        self.window.mainloop()
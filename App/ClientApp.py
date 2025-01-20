import tkinter as tk

class ClientApp:
    def __init__(self, klient):
        self.klient = klient
        self.window = tk.Tk()
        self.window.title(f"Panel Klienta - {klient.name}")

        self.label = tk.Label(self.window, text="Brak nowych lekcji")
        self.label.pack()

        self.update_button = tk.Button(self.window, text="Odśwież", command=self.refresh)
        self.update_button.pack()

    def refresh(self):
        self.label.config(text=f"Ostatnia lekcja: {self.klient.last_notification}")

    def notify(self, data):
        self.klient.last_notification = data
        self.label.config(text=f"Nowa lekcja: {data}")

    def run(self):
        self.window.mainloop()

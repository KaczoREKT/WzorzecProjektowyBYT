from Observer.Observer import Observer

class Klient(Observer):
    def __init__(self, poziom_zaawansowania):
        super().__init__()
        self.poziom_zaawansowania = poziom_zaawansowania

    def aktualizujInformacje(self, subject):
        print(f"Do systemu dodano nowy turniej o twoim poziomie zaawansowania: {self.poziom_zaawansowania}.")

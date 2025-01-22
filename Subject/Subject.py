class Subject:
    def __init__(self):
        self.subskrybenci = []
        self.poziom_zaawansowania = None  # Dodano atrybut z domyślną wartością

    def dodajSubskrybenta(self, observer):
        if observer not in self.subskrybenci:
            self.subskrybenci.append(observer)

    def usunSubskrybenta(self, observer):
        if observer in self.subskrybenci:
            self.subskrybenci.remove(observer)

    def powiadomSubskrybentow(self):
        for subskrybent in self.subskrybenci:
            subskrybent.aktualizujInformacje(self)

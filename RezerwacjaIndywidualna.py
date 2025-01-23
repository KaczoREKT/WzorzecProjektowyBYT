from Subject import Subject


class RezerwacjaIndywidualna(Subject):
    def __init__(self, data_rozpoczecia, data_zakonczenia, godzina_rozpoczecia, godzina_zakonczenia):
        super().__init__()
        self.data_rozpoczecia = data_rozpoczecia
        self.data_zakonczenia = data_zakonczenia
        self.godzina_rozpoczecia = godzina_rozpoczecia
        self.godzina_zakonczenia = godzina_zakonczenia
        self.subskrybenci = []

    def dodajSubskrybenta(self, observer):
        if observer not in self.subskrybenci:
            self.subskrybenci.append(observer)

    def usunSubskrybenta(self, observer):
        if observer in self.subskrybenci:
            self.subskrybenci.remove(observer)

    def powiadomSubskrybentow(self):
        for subskrybent in self.subskrybenci:
            subskrybent.aktualizujInformacje(self)

    # Użytkownik podaje nazwę atrybutu i jego nową wartość.
    # Jeśli podany atrybut jest poprawny, wartość jest zmieniana na nową.
    def zmienDaneRezerwacji(self, **kwargs):
        flag = False
        for attr, value in kwargs.items():
            if value is not None and hasattr(self, attr):
                setattr(self, attr, value)
                flag = True
            else:
                raise Exception("Podano złą nazwę atrybutu!")
        if flag:
            self.powiadomSubskrybentow()



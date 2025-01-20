from Observer.Observer import Observer


class Klient(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"{self.name}, nowa lekcja dostępna: {data}")
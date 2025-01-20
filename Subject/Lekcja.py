from Subject.Subject import Subject


class Lekcja(Subject):
    def __init__(self):
        self._observers = []
        self.lessons = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.lessons[-1])

    def add_lesson(self, data):
        self.lessons.append(data)
        self.notify()
# observer.py

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

class Logger:
    def update(self, message):
        print(f"[LOG] {message}")

class EmailNotifier:
    def update(self, message):
        print(f"[EMAIL] Notificación: {message}")

if __name__ == "__main__":
    subject = Subject()
    subject.attach(Logger())
    subject.attach(EmailNotifier())

    subject.notify("Usuario registrado con éxito")

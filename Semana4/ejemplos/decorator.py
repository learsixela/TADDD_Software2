# decorator.py

class Notifier:
    def send(self, message: str):
        print(f"Notificando: {message}")

# Decorador base
class NotifierDecorator(Notifier):
    def __init__(self, wrappee: Notifier):
        self.wrappee = wrappee

    def send(self, message: str):
        self.wrappee.send(message)

# Decoradores concretos
class SMSNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"[SMS] {message}")

class SlackNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"[Slack] {message}")

if __name__ == "__main__":
    base = Notifier()
    sms = SMSNotifier(base)
    slack = SlackNotifier(sms)

    slack.send("Nuevo login detectado!")

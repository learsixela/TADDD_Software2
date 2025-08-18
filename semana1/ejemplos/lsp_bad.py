class Bird:
    def fly(self):
        print("Flying...")

class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly!")  # Rompe el contrato de la clase base

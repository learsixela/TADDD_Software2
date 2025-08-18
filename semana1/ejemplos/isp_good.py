class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working...")
    def eat(self):
        print("Eating...")

class Robot(Workable):
    def work(self):
        print("Working 24/7...")

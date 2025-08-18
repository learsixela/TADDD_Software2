class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def eat(self):
        raise NotImplementedError("Robots don't eat!")

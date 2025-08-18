class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class NonFlyingBird(Bird):
    pass

class Ostrich(NonFlyingBird):
    pass

class Sparrow(FlyingBird):
    pass

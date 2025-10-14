class Flyweight:
    def __init__(self, state):
        self.state = state

    def display(self, extrinsic_state):
        print(f"Flyweight state: {self.state}, extrinsic state: {extrinsic_state}")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, state):
        if state not in self._flyweights:
            self._flyweights[state] = Flyweight(state)
        return self._flyweights[state]


factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("Shared State 1")
flyweight1.display("External Data 1")

flyweight2 = factory.get_flyweight("Shared State 1")
flyweight2.display("External Data 2")

flyweight3 = factory.get_flyweight("Shared State 2")
flyweight3.display("External Data 3")

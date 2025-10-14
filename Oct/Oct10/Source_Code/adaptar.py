class OldSystem:
    def old_method(self):
        return "Old Method"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return f"Adapter: {self.old_system.old_method()}"

old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.new_method())

class CPU:
    def start(self):
        print("CPU Starting")

class Memory:
    def load(self):
        print("Memory Loading")

class HardDrive:
    def read(self):
        print("Reading from Hard Drive")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        print("Computer Started")

computer = ComputerFacade()
computer.start_computer()

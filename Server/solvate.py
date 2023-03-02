class Solvate(GromacsProcess):
    def __init__(self,arguments):
        self.process = None
        self.command = "solvate"
        self.inputString = []
        self.arguments = arguments
        self.process = None


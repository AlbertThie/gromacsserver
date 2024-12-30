import os
from .GromacsProcess import GromacsProcess

class Solvate(GromacsProcess):
    def __init__(self,arguments):
        self.process = None
        self.command = "solvate"
        self.inputString = []
        self.arguments = arguments
        self.process = None


    def createInputString(self):
        inputString = [str(self.command)]
        for k, v in self.arguments.items():
            print("solvate is doing :"  + (str(k) + "   " +str(v)))
            if k == "solvatetype":
                inputString = inputString + self.createString("-cs",(str(v)+ ".gro"))
            elif k == "topology":
                inputString = inputString + self.createString("-p",str(v))
            else:
                inputString = inputString + self.createString(k,v)


        self.inputString = inputString

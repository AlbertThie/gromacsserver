import os
from .GromacsProcess import GromacsProcess


class EditConf(GromacsProcess):
    def __init__(self,arguments):
        self.process = None
        self.command = "editconf"
        self.inputString = []
        self.arguments = arguments
        self.process = None

    def createInputString(self):
        inputString = [str(self.command)]
        for k, v in self.arguments.items():
            if k == "boundary":
                inputString = inputString + self.createString("-d",str(v))
            elif k == "boxType":
                inputString = inputString + self.createString("-bt",v)
            elif k == "centered":
                inputString = inputString + self.createString("-c","True")
            else:
                inputString = inputString + self.createString(k,v)

        self.inputString = inputString

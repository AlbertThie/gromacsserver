import os
from GromacsProcess import GromacsProcess


class EditConf(GromacsProcess):
    def __init__(self,arguments):
        self.process = None
        self.command = "editconf"
        self.inputString = []
        self.arguments = arguments
        self.process = None

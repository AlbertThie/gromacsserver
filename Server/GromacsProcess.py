import subprocess


class GromacsProcess:

    def __init__(self):
        self.command = None
        self.inputString = []
        self.arguments= {}
        self.process = None



    def createInputString(self):
        inputString = [str(self.command)]
        for k, v in self.arguments.items():
            print("GromacsProcess is doing :"  + (str(k) + "   " +str(v)))
            inputString = inputString + self.createString(k,v)

        self.inputString = inputString

    def getInputString(self):
        return self.inputString
        
    def createString(self,key,value):
        return [str(key),str(value)]













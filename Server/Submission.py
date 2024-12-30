import os
from .Calculation import Calculation
from .EditConf import EditConf


class Submission:
    def __init__(self,request):
        self.request = request
        self.calculation = Calculation()
        self.gromacsCommand = getCalculationType()


    def getCalculation(self):
        return self.calculation

    def getGromacsCommand(self):
        return self.gromacsCommand
        
    def getCalculationType(self):
        if(self.request["jobType"] =="EditConf"):
            return EditConf(json.loads(editconfparameters['json']))



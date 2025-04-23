import os
from .Calculation import Calculation
from .EditConf import EditConf


class Submission:
    def __init__(self,request):
        self.request = request
        print(f"Request is {request}")
        if(self.request["jobType"] =="EditConf"):
            self.gromacsCommand = "editconf"
            self.calc_process = EditConf(request)
            self.calculation = Calculation(self.calc_process)

    def getCalculation(self):
        return self.calculation

    def getGromacsCommand(self):
        return self.gromacsCommand
        
    def getCalculationType(self):
        return self.calc_process


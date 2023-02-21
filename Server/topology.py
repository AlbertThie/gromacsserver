import shutil
import os
from GromacsProcess import GromacsProcess




class Pdb2gmx(GromacsProcess):
    def __init__(self,input_list,output_list):
        self.command = "pdb2gmx"
        self.input_list = input_list
        self.output_list = output_list
        self.inputString = []
        self.arguments= {"-f": input_list,"-o": output_list}
        self.process = None

    def setWater(self,value):
        self.arguments["-water"] = value

    def getWater(self):
        return self.arguments["-water"]


    def setForceField(self,value):
        self.arguments["-ff"] = value


    def getForceField(self):
        return self.arguments["-ff"]


"""
def pdb2gmx (inputfile, outputfile, watertype,forcefield):
    print("Init forcefield")
    process = gmx.commandline_operation('gmx',
                                    arguments=["pdb2gmx","-water",watertype,"-ff",forcefield],
                                    input_files ={'-f':'../'+inputfile},
                                    output_files ={'-o':outputfile},cwd=os.getcwd())

    if process.output.returncode.result() !=0:
        print(process.output.stderr.result())
   # subprocessimporter(process.output.directory.result())
"""


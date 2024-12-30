import os
from .GromacsProcess import GromacsProcess




class Pdb2gmx(GromacsProcess):
    def __init__(self,arguments):
        self.process = None
        self.command = "pdb2gmx"
        self.inputString = []
        self.arguments = arguments
        self.process = None


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


import shutil
import os
import itertools
from werkzeug.utils import secure_filename

class Calculation():
    calculations = {}
    newid = itertools.count()
    def __init__(self):
        self.id = next(Calculation.newid)


    def getId(self):
        return self.id

    def saveFiles(self,f,name):

        self.directory = os.getcwd()+'/Calculations/' + str(self.id)+'/'
        try:
            os.makedirs(self.directory)
        except OSError:
            pass
        if isinstance(f, str):
            text_file = open(name, "w")
            text_file.write(f)
            text_file.close()
        else:
            f.save(os.path.join(self.directory , secure_filename(f.filename)))
        return self.directory

    def getDirectory(self):
        return self.directory

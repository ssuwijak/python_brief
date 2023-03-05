#import os
from pathlib import Path

class DirInfo:
    def __init__(self, fullPath:str):
        self._fullPath = fullPath.strip()

    def __str__():
        return self.FullPath        

    @property
    def FullPath(self):
        return self._fullPath
    
    @FullPath.setter
    def FullPath(self, value):
        value = value.strip()
        if self.Exists():
            self._fullPath = value
        


    def Exists(self):
        return Path.exists(self._fullPath)


    def GetAll(self):
        p = Path('.')
        return [x for x in p.iterdir()]
        
    def GetDirectories(self):
        p = Path('.')
        return [x for x in p.iterdir() if x.is_dir()]

    def GetFiles(self):
        p = Path('.')
        return [x for x in p.iterdir() if x.is_file()] 


if __name__ == '__main__':
    pass
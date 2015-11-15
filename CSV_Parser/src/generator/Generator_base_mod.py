'''
Created on 2015-11-01

@author: tomar
'''

class BaseGeneratorException(Exception):
    """Base class for BaseGeneratorException related exceptions."""

class BaseGenerator(object):
   
    def __init__(self, fileName = ''):
        self.reset()
        self.setFile(fileName)
        
    def reset(self):
        self.setFile('', True)
        self.outFile = None
        
    def setFile(self, fileName='', force=False):
        if force or fileName != '':
            self.fileName = fileName
            
    def generate(self, fileName = ''):
        self.setFile(fileName)
        
        if self.fileName != '':
            self.outFile = open(self.fileName, 'w')
            self.preProcess()
            self.process()
            self.postProcess()
            self.outFile.close()
    
    def preProcess(self):
        pass

    def process(self):
        pass
    
    def postProcess(self):
        pass


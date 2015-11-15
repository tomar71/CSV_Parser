'''
Created on 2015-11-01

@author: tomar
'''

class BaseParserException(Exception):
    """Base class for BaseParserException related exceptions."""

class BaseParser(object):
   
    def __init__(self, fileName = ''):
        self.reset()
        self.setFile(fileName)
        
    def reset(self):
        self.setFile('', True)
        
    def setFile(self, fileName='', force=False):
        if force or fileName != '':
            self.fileName = fileName
    
    def getFileName(self):
        return self.fileName      
      
    def parse(self, fileName = ''):
        self.setFile(fileName)
        fileName = self.getFileName()
        self.reset()
        self.setFile(fileName)
        
        if self.fileName != '':
            self.preProcess()
            self.process()
            self.postProcess()
    
    def preProcess(self):
        pass

    def process(self):
        pass
    
    def postProcess(self):
        pass


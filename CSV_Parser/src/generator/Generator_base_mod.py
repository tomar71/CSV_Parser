'''
Created on 2015-11-01

@author: tomar
'''
from src.entity import csvDictionary_mod

class BaseGeneratorException(Exception):
    """Base class for BaseGeneratorException related exceptions."""

class BaseGenerator(object):
   
    def __init__(self, fileName = ''):
        self.reset()
        self.setFile(fileName)
        
    def reset(self):
        self.setFile('', True)
        self.outFile = None
        self.csvDataDict = None
        self.totalLineCount = 0
                
    def setFile(self, fileName='', force=False):
        if force or fileName != '':
            self.fileName = fileName

    def addData(self, csvDataDict):
        if isinstance(csvDataDict, csvDictionary_mod.CSVDictionary):
            self.csvDataDict = csvDataDict
            return True
        return False
            
    def generate(self, fileName = ''):
        self.setFile(fileName)
        
        if self.fileName != '':
            self.outFile = open(self.fileName, 'w')
            self.preProcess()
            self.process()
            self.postProcess()
            self.outFile.close()

    def generateLine(self, csvLineData):
        if csvLineData != None and isinstance(csvLineData, list):
            return True
        return False

    def generateHeaderLine(self, csvLineData):
        return self.generateLine(csvLineData)
    
    def process(self):
        if self.csvDataDict != None and isinstance(self.csvDataDict, csvDictionary_mod.CSVDictionary):
            for lineId in range(0, self.csvDataDict.getNumRows()):
                if(lineId == 0):
                    self.generateHeaderLine(self.csvDataDict.getRowData(lineId))
                else:
                    self.generateLine(self.csvDataDict.getRowData(lineId))
                self.totalLineCount = self.totalLineCount + 1
    
    def preProcess(self):
        pass
    
    def postProcess(self):
        pass

    def getTotalLinesCount(self):
        return self.totalLineCount

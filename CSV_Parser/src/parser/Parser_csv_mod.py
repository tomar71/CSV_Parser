'''
Created on 2015-11-01

@author: tomar
'''

from src.parser import Parser_base_mod
from src.entity import csvDictionary_mod

class ParserException(Exception):
    """Base class for ParserException related exceptions."""
    
class Parser(Parser_base_mod.BaseParser):
    
    def __init__(self, fileName = ''):
        super(Parser, self).__init__(fileName)
        
    def reset(self):
        super(Parser, self).reset()
        self.totalLineCount = 0
        self.totalValidLineCount = 0
        self.csvDict = csvDictionary_mod.CSVDictionary()
        
    def getTotalLinesCount(self):
        return self.totalLineCount

    def getTotalValidLinesCount(self):
        return self.totalValidLineCount

    def isValidLine(self,csvLine):
        return True

    def getLinesFromFile(self):
        if(self.fileName != ''):
            csvFile = open(self.fileName, 'r')
            lines = csvFile.readlines()
            csvFile.close()
            return lines
        return None

    def process(self):
        lines = self.getLinesFromFile()
        if lines!= None and len(lines) > 0:
            self.totalLineCount = len(lines)
            for csvLine in lines:
                line = csvLine.split('\n')[0]
                self.processLine(line)
                
    
    def processLine(self, csvLine):
        if self.isValidLine(csvLine):
            lineWords_dict = csvLine.split(',')
            self.csvDict.addRowData(self.totalValidLineCount, lineWords_dict)
            self.totalValidLineCount = self.totalValidLineCount + 1
    
    def getLineData(self, lineNumber):
        return self.csvDict.getRowData(lineNumber)
    
    def getData(self):
        return self.csvDict
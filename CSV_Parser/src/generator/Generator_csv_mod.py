from src.generator import Generator_base_mod
from src.entity import csvDictionary_mod

class GeneratorException(Exception):
    """Base class for GeneratorException related exceptions."""
    
class Generator(Generator_base_mod.BaseGenerator):
    
    def reset(self):
        super(Generator, self).reset()
        self.totalLineCount = 0
        self.csvDict = None
    
    def addData(self, csvData):
        if isinstance(csvData, csvDictionary_mod.CSVDictionary):
            self.csvDict = csvData
    
    def generateLine(self, csvLineData):
        if csvLineData != None and isinstance(csvLineData, list):
            lineTxt = ''
            for wordId in range(0, len(csvLineData)):
                if wordId > 0:
                    lineTxt = lineTxt + ',' +csvLineData[wordId]
                else:
                    lineTxt = csvLineData[wordId]
            self.outFile.write(lineTxt+'\n')
    
    def process(self):
        if self.csvDict != None and isinstance(self.csvDict, csvDictionary_mod.CSVDictionary):
            for lineId in range(0, self.csvDict.getNumRows()):
                self.generateLine(self.csvDict.getRowData(lineId))
                self.totalLineCount = self.totalLineCount + 1
            
    def getTotalLinesCount(self):
        return self.totalLineCount
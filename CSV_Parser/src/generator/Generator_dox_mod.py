from src.generator import Generator_base_mod
from src.entity import csvDictionary_mod

class GeneratorException(Exception):
    """Base class for GeneratorException related exceptions."""
    
class Generator(Generator_base_mod.BaseGenerator):
    
    def reset(self):
        super(Generator, self).reset()
        self.totalLineCount = 0
        self.dataDict = None
        self.maxColumnCount = 0
        self.maxColumnWidth_dict = {}
    
    def addData(self, dataDict):
        if isinstance(dataDict, csvDictionary_mod.CSVDictionary):
            self.dataDict = dataDict
            for lineId in range(0, self.dataDict.getNumRows()):
                csvLineData = self.dataDict.getRowData(lineId)
                if csvLineData != None and isinstance(csvLineData, list):
                    if(len(csvLineData) > self.maxColumnCount):
                        self.maxColumnCount = len(csvLineData)
                    for colId in range(0, len(csvLineData)):
                        if(colId not in self.maxColumnWidth_dict.keys()):
                            self.maxColumnWidth_dict[colId] = len('----')
                        if(len(csvLineData[colId]) > self.maxColumnWidth_dict[colId]):
                            self.maxColumnWidth_dict[colId] = len(csvLineData[colId])
    
    def wordLengthAdjust(self, wordVal, columnId):
        for spaceCount in range(0, self.maxColumnWidth_dict[columnId] - len(wordVal)):
            wordVal = wordVal +' '
        return wordVal
    
    def generateLine(self, csvLineData):
        if csvLineData != None and isinstance(csvLineData, list):
            lineTxt = ''
            for wordId in range(0, len(csvLineData)):
                wordVal = csvLineData[wordId]
                    
                if wordVal == '':
                    wordVal = '-'

                wordVal = self.wordLengthAdjust(wordVal, wordId)
                
                if wordId > 0:
                    lineTxt = lineTxt + '|' + wordVal
                else:
                    lineTxt = wordVal
            if (len(csvLineData) < self.maxColumnCount):
                for wordId in range(0, self.maxColumnCount - len(csvLineData)):
                    lineTxt = lineTxt + '|-'
            self.outFile.write(lineTxt+'\n')

    def generateHeaderLine(self):
        lineTxt = ''
        for wordId in range(0, self.maxColumnCount):
            wordVal = '----'
            wordVal = self.wordLengthAdjust(wordVal, wordId)
            if (wordId == 0):
                lineTxt = lineTxt + wordVal
            else:
                lineTxt = lineTxt + '|' + wordVal
            
        self.outFile.write(lineTxt+'\n')
    
    def process(self):
        if self.dataDict != None and isinstance(self.dataDict, csvDictionary_mod.CSVDictionary):
            for lineId in range(0, self.dataDict.getNumRows()):
                self.generateLine(self.dataDict.getRowData(lineId))
                if(lineId == 0):
                    self.generateHeaderLine()
                self.totalLineCount = self.totalLineCount + 1
            
    def getTotalLinesCount(self):
        return self.totalLineCount
from src.generator import Generator_base_mod
from src.entity import csvDictionary_mod

class GeneratorException(Exception):
    """Base class for GeneratorException related exceptions."""
    
class Generator(Generator_base_mod.BaseGenerator):
    
    def generateLine(self, csvLineData):
        if(super(Generator, self).generateLine(csvLineData)):
            lineTxt = ''
            for wordId in range(0, len(csvLineData)):
                if wordId > 0:
                    lineTxt = lineTxt + ',' +csvLineData[wordId]
                else:
                    lineTxt = csvLineData[wordId]
            self.outFile.write(lineTxt+'\n')
            

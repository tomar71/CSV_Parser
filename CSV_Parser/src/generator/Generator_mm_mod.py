from src.generator import Generator_base_mod
from src.generator.util import util_xml_mod

class GeneratorException(Exception):
    """Base class for GeneratorException related exceptions."""
    
class Generator(Generator_base_mod.BaseGenerator):
    
    def reset(self):
        super(Generator, self).reset()
        self.xmlUtil = None
    
    def addData(self, dataDict):
        if(super(Generator, self).addData(dataDict)):
            pass
    
    def preProcess(self):
        super(Generator, self).preProcess()
        self.xmlUtil = util_xml_mod.util(self.outFile)
            
    def generateLine(self, csvLineData):
        if(super(Generator, self).generateLine(csvLineData)):
            if len(csvLineData) > 0 and (len(csvLineData[0]) > 0 and len(csvLineData[0].split(' ')) > 0):
                self.xmlUtil.openElementWAtt('node')
                for wordId in range(0, len(csvLineData)):
                    wordVal = csvLineData[wordId]
                    
                    if wordId > 0:
                        self.xmlUtil.openElementWAtt('attribute')
                        self.xmlUtil.addAttribute('att'+str(wordId), wordVal)   
                        self.xmlUtil.endElementWAtt()
                    else:
                        self.xmlUtil.addAttribute('TEXT', wordVal)   
                        self.xmlUtil.endElementWAtt()
                self.xmlUtil.closeElement('node')
                return True
        return False

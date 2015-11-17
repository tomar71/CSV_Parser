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
        
        self.xmlUtil.openElementWAtt('map')
        self.xmlUtil.addAttribute('version', '0.9.0')
        self.xmlUtil.endElementWAtt()
        self.xmlUtil.newLn()
        
        self.xmlUtil.openElementWAtt('node')
        self.xmlUtil.addAttribute('TEXT', 'ROOT')
        self.xmlUtil.endElementWAtt()
        self.xmlUtil.newLn()
        
    def generateLine(self, csvLineData):
        offset = 4
        if(super(Generator, self).generateLine(csvLineData)):
            if len(csvLineData) > 0 and (len(csvLineData[0]) > 0 and len(csvLineData[0].split(' ')) > 0):
                self.xmlUtil.openElementWAtt('node', offset)
                
                for wordId in range(0, len(csvLineData)):
                    wordVal = csvLineData[wordId]
                    
                    if wordId > 0:
                        self.xmlUtil.openElementWAtt('attribute', offset*2)
                        self.xmlUtil.addAttribute('NAME', 'att'+str(wordId))
                        self.xmlUtil.addAttribute('VALUE', wordVal)   
                        self.xmlUtil.closeElementImmediate()
                        self.xmlUtil.newLn()
                    else:
                        self.xmlUtil.addAttribute('TEXT', wordVal)   
                        self.xmlUtil.endElementWAtt()
                        self.xmlUtil.newLn()
                        
                self.xmlUtil.closeElement('node', offset)
                self.xmlUtil.newLn()
                return True
        return False

    def postProcess(self):
        Generator_base_mod.BaseGenerator.postProcess(self)
        
        self.xmlUtil.closeElement('node')
        self.xmlUtil.newLn()
        
        self.xmlUtil.closeElement('map')
        self.xmlUtil.newLn()
from src.generator import Generator_base_mod

class GeneratorException(Exception):
    """Base class for GeneratorException related exceptions."""
    
class Generator(Generator_base_mod.BaseGenerator):
    
    def reset(self):
        super(Generator, self).reset()
        pass
    
    def addData(self, dataDict):
        if(super(Generator, self).addData(dataDict)):
            pass
    
    def generateLine(self, csvLineData):
        if(super(Generator, self).generateLine(csvLineData)):
            return True
        return False

    def generateHeaderLine(self, csvLineData):
        if(super(Generator, self).generateHeaderLine(csvLineData)):
            pass
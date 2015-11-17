class util(object):
    
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        
    def newLn(self):   
        self.xmlFile.write('\n')
    
    def addTxt(self, txt=""):
        if len(str(txt)) > 0 :   
            self.xmlFile.write(txt)
        
    def openElementWoAtt(self, element, offset = 0):
        self.addOffset(offset)
        self.xmlFile.write('<'+element+'>')
            
    def closeElement(self, element, offset = 0):
        self.addOffset(offset)   
        self.xmlFile.write('</'+element+'>')
        
    def openElementWAtt(self, element, offset = 0):
        self.addOffset(offset)   
        self.xmlFile.write('<'+element)
    
    def addAttribute(self, attName, attValue):   
        self.xmlFile.write(' '+attName+'="'+attValue+'" ')
    
    def endElementWAtt(self):   
        self.xmlFile.write('>')

    def closeElementImmediate(self):   
        self.xmlFile.write('/>')
        
    def closeElementWAtt(self, element, offset = 0):   
        self.endElementWAtt(element)
        self.newLn()
        self.closeElement(element, offset)
        
    def openCloseElementImmediate(self, element, offset = 0): 
        self.openElementWAtt(element, offset)
        self.xmlFile.write('/>')
        
    def addOffset(self, offset = 0):
        space=""
        for i in range(0,offset):
            space = space + ' '
        self.xmlFile.write(space)
        
class util(object):
    
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        
    def newLn(self):   
        self.xmlFile.write('\n')
    
    def addTxt(self, txt=""):
        if len(str(txt)) > 0 :   
            self.xmlFile.write(txt)
        
    def openElementWoAtt(self, element):   
        self.xmlFile.write('<'+element+'>')
            
    def closeElement(self, element):   
        self.xmlFile.write('</'+element+'>')
        
    def openElementWAtt(self, element):   
        self.xmlFile.write('<'+element)
    
    def addAttribute(self, attName, attValue):   
        self.xmlFile.write(' '+attName+'="'+attValue+'" ')
    
    def endElementWAtt(self):   
        self.xmlFile.write('>')
        
    def closeElementWAtt(self, element):   
        self.endElementWAtt(element)
        self.newLn()
        self.closeElement(element)
        
    def openCloseElementImmediate(self, element): 
        self.openElementWAtt(element)
        self.xmlFile.write('/>')
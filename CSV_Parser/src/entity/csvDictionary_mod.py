'''
Created on 2015-11-01

@author: tomar
'''

class CSVDictionary(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.rowData_dict = {}
    
    def addRowData(self, rowNumber, rowData):
        if isinstance(rowNumber, int): 
            self.rowData_dict[rowNumber] = rowData
            
    def getRowData(self, rowNumber):
        if isinstance(rowNumber, int) and (rowNumber in self.rowData_dict.keys()):
            return self.rowData_dict[rowNumber]
        else:
            return None
        
    def getNumRows(self):
        return len(self.rowData_dict)
    
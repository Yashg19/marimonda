'''
Created on 25/05/2009

@author: yllanos
'''

class Persona:
    '''
    classdocs
    '''


    def __init__(self, nombre):
        '''
        Constructor
        '''
        self.nombre = nombre
        
    def inform(self):
        print self.nombre
    
        
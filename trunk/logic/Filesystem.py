'''
Created on 24/05/2009

@author: yllanos
'''

class Filesystem():
    '''
    classdocs
    '''

    maxnFiles = 0   #Maximum number of files supported
    maxVolSize = 0  #Maximum partition Size
    filenameLength = 0 #Maximum number of characters supported for file name
    perm = Permissions() 

    def __init__(selfparams):
        '''
        Constructor
        '''
        
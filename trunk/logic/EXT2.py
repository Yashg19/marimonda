'''
Created on 24/05/2009

@author: yllanos
'''

class EXT2():
    '''
    classdocs
    '''

    superBlock = EXT2SuperBlock()
    blockGroups = []
    partitionSize = 0
    blockSize = 512
    nBlockGroups = 0    #Number of block groups
    

    def __init__(selfparams):
        '''
        Constructor
        '''
        
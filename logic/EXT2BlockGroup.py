'''
Created on 24/05/2009

@author: yllanos
'''

class EXT2BlockGroup():
    '''
    classdocs
    '''

    InodeTable = []
    SuperBlock = EXT2SuperBlock()
    GroupDescriptor = EXT2GroupDescriptor()
    dataBlocksBitmap = []
    inodeBitmap = []

    def __init__(selfparams):
        '''
        Constructor
        '''
        
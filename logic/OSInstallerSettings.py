'''
Created on 26/05/2009

@author: yllanos
'''

class OSInstallerSettings():
    '''
    Settings class for the EXT2 Filesystem
    '''
    partitionSize = 21474836480 #20GB
    blockSize = 2048 #2048 bytes block
    nBlockGroups = int(partitionSize/(8*blockSize*blockSize))
    mean = 1024     #Mean file size
    stdDev = 3.2    #Standard deviation
    blocksPerGroup = 8*blockSize
    inodesPerGroup = 8*blocksPerGroup
    nOperations = 300000

    def __init__(selfparams):
        '''
        Constructor
        '''
        
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 26/05/2009

@author: yllanos
'''

from Lognormal import *
from Pareto import *
from Zipf import *

class EXT2InstallerSettings():
    '''
    Settings class for the EXT2 Filesystem
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.partitionSize = 21474836480 #20GB
        self.blockSize = 1024 #1024-bytes block
        self.nBlockGroups = int(partitionSize/(8*blockSize*blockSize))
        self.blocksPerGroup = 8*blockSize
        self.inodesPerGroup = 8*blocksPerGroup
        self.nOperations = 300000
        self.targetDistribution = Lognormal()
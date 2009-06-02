#!/usr/bin/env python
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
    partitionSize = 21474836480 #20GB
    blockSize = 1024 #1024-bytes block
    nBlockGroups = int(partitionSize/(8*blockSize*blockSize))    
    blocksPerGroup = 8*blockSize
    inodesPerGroup = 8*blocksPerGroup
    nOperations = 300000
    targetDistribution = Lognormal()

    def __init__(selfparams):
        '''
        Constructor
        '''
        
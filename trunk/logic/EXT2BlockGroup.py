# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 24/05/2009

@author: yllanos
'''

from Inode import *
from EXT2 import *
from math import *

class EXT2BlockGroup():
    '''
    This class represents a single Block Group
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.inodeTable = {}
        self.inodeBitmap = {}
        self.dataBlocksBitmap = {}
        self.groupDescriptor = EXT2GroupDescriptor()
        self.groupDescriptor.bgFreeBlocksCount = osSettings.nBlockGroups
        self.groupDescriptor.bgFreeInodesCount = osSettings.inodesPerGroup
        self.groupDescriptor.i_prealloc_block = osSettings.prealloc_blocks        
    
    def find_blocks_prealloc(self,blocksNeeded):
        '''
        This function should receive a target number of blocks
        to preallocate and returns a list with the continuous blocks.
        '''
        return None
        
    def find_blocks_no_prealloc(self,blocksNeeded):
        '''
        
        '''
        return None

    def has_available_blocks(self):
        '''

        '''
        return None


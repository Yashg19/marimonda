#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 24/05/2009

@author: yllanos
'''

from Inode import *
from EXT2 import *

class EXT2BlockGroup():
    '''
    This class represents a single Block Group
    '''

    InodeTable = {}
    dataBlocksBitmap = []
    inodeBitmap = []
    groupDescriptor = EXT2GroupDescriptor()
    groupDescriptor.bgFreeBlocksCount = osSettings.nBlockGroups
    groupDescriptor.bgFreeInodesCount = osSettings.inodesPerGroup

    def __init__(selfparams):
        '''
        Constructor
        '''
        
    def create_inode(self):
        '''
        
        '''
        return Inode()        
        
    def find_block(self):
        '''
        
        '''
        if 1>2:
            return None
        else:
            return False
    
    def find_block_prealloc(self):
        '''
        
        '''
        return None
        
    def find_block_no_prealloc(self):
        '''
        
        '''
        return None
        
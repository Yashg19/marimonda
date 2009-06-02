#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 24/05/2009

@author: yllanos
'''

from EXT2SuperBlock import *
from EXT2BlockGroup import *
from EXT2Installer import *
from Filesystem import *

class EXT2(Filesystem):
    '''
    classdocs
    '''

    superBlock = EXT2SuperBlock()
    blockGroups = {}
    partitionSize = osSettings.partitionSize
    blockSize = osSettings.blockSize
    nBlockGroups = osSettings.nBlockGroups    #Number of block groups
    

    def __init__(selfparams):
        '''
        Constructor
        '''
        
    def create_file(self, fileSize):
        '''
        
        '''
        group = find_group()
        if group != None:
            pass
        else:
            pass
        return None
        
    def delete_file(self, inode):
        '''
        
        '''        
        return None

    def find_group(self):
        '''
        Search the whole file system 
        for a block group with free blocks
        '''
        if len(blockGroups.keys())==0:  #Means the file system is empty, so start on block group 0
            return 0
            '''
            blockGroups = {0:EXT2BlockGroup()}
            findBlockResult = blockGroups[0].find_block()
            if findBlockResult[0] == True:
                blockGroups[0].InodeTable[0] = blockGroups[0].create_inode()
            '''
        else:
            pass        
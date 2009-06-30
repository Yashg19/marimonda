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

    inodeTable = {}
    inodeBitmap = {}
    dataBlocksBitmap = {}
    groupDescriptor = EXT2GroupDescriptor()
    groupDescriptor.bgFreeBlocksCount = osSettings.nBlockGroups
    groupDescriptor.bgFreeInodesCount = osSettings.inodesPerGroup

    def __init__(selfparams):
        '''
        Constructor
        '''
        
    def create_inode(self, filesize):     #Debería crear los bloques del archivo de una vez
        '''
        This method creates the inode for every file and
        also creates the associated blocks by calling the
        get_blocks() method.
        It returns an Inode object.
        '''
        newInode = Inode()
        if inodeTable.__len__() > 0:
            newInode.i_inode = inodeTable.__len__() + 1
        else:
            newInode.i_inode = 0
        newInode.i_isize = filesize
        if filesize < osSettings.blockSize:
            blocksNeeded = 1
        elif (filesize % osSettings.blockSize) > 0:
            blocksNeeded = int(filesize/osSettings.blockSize) + 1
        elif (filesize % osSettings.blockSize) == 0:
            blocksNeeded = int(filesize/osSettings.blockSize)
        newInode.i_iblock = get_blocks(blocksNeeded)
        return newInode

    def fill_direct_blocks(self, blocksNeeded):
        '''

        '''
        i = 1
        directBlocksList = []
        while i <= blocksNeeded:
            directBlocksList.append(find_block())
            i = i + 1
        return directBlocksList

    def fill_first_indirect_blocks(self,blocksNeeded):
        '''
        '''
        i = 1
        firstIndirectList = []
        firstIndirectList.append(fill_direct_blocks(blocksNeeded))
        return firstIndirectList
        
    def find_block(self):
        '''
        
        '''
        return None
    
    def find_block_prealloc(self):
        '''
        
        '''
        return None
        
    def find_block_no_prealloc(self):
        '''
        
        '''
        return None

    def get_blocks(self,blocksNeeded):
        '''
        Calculates and creates the number of needed inodes for a file,
        including both the direct and indirect ones.
        It returns a list with the blocks.
        '''
        firstIndirection = (osSettins.blockSize/4) + 11
        secondIndirection = ((osSettings.blockSize/4)*(osSettings.blockSize/4)) + firstIndirection
        thirdIndirection = ((osSettings.blockSize/4)*(osSettings.blockSize/4)*(osSettings.blockSize/4)) + secondIndirection
        if blocksNeeded <= 12:  #Direct addressing
            return fill_direct_blocks(blocksNeeded)
        else:
            blocksList = []
            blocksList.append(fill_direct_blocks(blocksNeeded))
            if blocksNeeded > 12 and blocksNeeded <= firstIndirection #1st-Indirection
                blocksList.append(fill_first_indirect_blocks(blocksNeeded-12))
                return blocksList
            else:
                if blocksNeeded > firstIndirection + 1 and blocksNeeded <= secondIndirection   #2nd-Indirection
                    pass
                if blocksNeeded > secondIndirection + 1 and blocksNeeded <= thirdIndirection  #3rd-Indirection
                    pass

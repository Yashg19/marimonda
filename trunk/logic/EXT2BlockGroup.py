#!/usr/bin/env python
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
        This method fills a list with the blocks
        directly addressed by the file system.
        Usually addresses blocks 1 to 12.
        '''
        i = 1
        directBlocksList = []
        while i <= blocksNeeded:
            directBlocksList.append(find_block())
            i = i + 1
        return directBlocksList

    def fill_first_indirect_blocks(self,blocksNeeded):
        '''
        This method fills both the direct and indirect blocks and
        returns a hierarchical list representing the 1st-level redirection
        '''
        firstIndirectList = []
        firstIndirectList.append(fill_direct_blocks(blocksNeeded))
        return firstIndirectList

    def fill_second_indirect_blocks(self,blocksNeeded):
        '''
        Similar to fill_first_indirect_blocks(), but on a higher,
        deeper, hierarchical level.
        '''
        secondIndirectList = []
        firstIndirectSets = int(ceil(blocksNeeded/12))  #to compute how many 1st-indirect sets of blocks in groups of 12 we need
        if blocksNedded > 12:
            i = 1
            while i <= firstIndirectSets:
                firstIndirectList = []
                secondIndirectList.append(firstIndirectList.append(fill_first_indirect_blocks(12)))
                i = i + 1
            remaining = blocksNeeded - (12*firstIndirectSets)
            secondIndirectList.append(firstIndirectList.append(fill_first_indirect_blocks(remaining)))
            return secondIndirectList
        else:
            return secondIndirectList.append(firstIndirectList.append(fill_first_indirect_blocks(blocksNeeded)))

    def fill_third_indirect_blocks(self, blocksNeeded):
        '''
        Similar to fill_second_indirect_blocks(), but higher in the hierarchy.
        It returns a hierarchical list with 3rd-level blocks indirection.
        '''
        thirdIndirectList = []
        if blocksNeeded > 12:
            pass
        else:
            secondIndirectList = []
            return thirdIndirectList.append(secondIndirectList.append(fill_second_indirect_blocks(blocksNeeded)))

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
                if blocksNeeded > firstIndirection and blocksNeeded <= secondIndirection   #2nd-Indirection
                    blocksList.append(fill_first_indirect_blocks(blocksNeeded-12))
                    blocksList.append(fill_second_indirect_blocks(blocksNeeded - 12 - firstIndirection))
                    return blocksList
                else:
                    if blocksNeeded > secondIndirection and blocksNeeded <= thirdIndirection  #3rd-Indirection
                        blocksList.append(fill_first_indirect_blocks(blocksNeeded-12))
                        blocksList.append(fill_second_indirect_blocks(blocksNeeded - 12 - firstIndirection))
                        blocksList.append(fill_third_indirect_blocks(blocksNeeded - 12 - firstIndirection - secondIndirection))
                        return blocksList

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
        
    def fill_direct_blocks(self, blocksNeeded):
        '''
        This method fills a list with the blocks
        directly addressed by the file system.
        Usually addresses blocks 1 to 12.
        '''
        i = 1
        directBlocksList = []
        while i <= blocksNeeded:
            directBlocksList.append(self.find_block_prealloc())
            i = i + 1
        return directBlocksList

    def fill_first_indirect_blocks(self,blocksNeeded):
        '''
        This method fills both the direct and indirect blocks and
        returns a hierarchical list representing the 1st-level redirection
        '''
        firstIndirectList = []
        firstIndirectList.append(self.fill_direct_blocks(blocksNeeded))
        return firstIndirectList

    def fill_second_indirect_blocks(self,blocksNeeded):
        '''
        Similar to fill_first_indirect_blocks(), but on a higher,
        deeper, hierarchical level.
        '''
        secondIndirectList = []
        firstIndirectSets = int(ceil(blocksNeeded/12))  #to compute how many 1st-indirect sets of blocks in groups of 12 we need
        if blocksNedded > 12:
            i = 1  #should be 1 because firstIndirectSets starts at set 0
            while i <= firstIndirectSets:
                firstIndirectList = []
                secondIndirectList.append(firstIndirectList.append(self.fill_first_indirect_blocks(12)))
                i = i + 1
            remaining = blocksNeeded - (12*firstIndirectSets)
            if remaining > 0:
                secondIndirectList.append(firstIndirectList.append(self.fill_first_indirect_blocks(remaining)))
            return secondIndirectList
        else:
            return secondIndirectList.append(firstIndirectList.append(self.fill_first_indirect_blocks(blocksNeeded)))

    def fill_third_indirect_blocks(self, blocksNeeded):
        '''
        Similar to fill_second_indirect_blocks(), but higher in the hierarchy.
        It returns a hierarchical list with 3rd-level blocks indirection.
        '''
        thirdIndirectList = []
        secondIndirectSets = int(ceil(blocksNeeded/144))  #to compute how many 2nd-indirect block sets we need
        if blocksNeeded > 144:
            i = 1
            while i <= secondIndirectSets:
                secondIndirectList = []
                thirdIndirectList.append(secondIndirectList.append(self.fill_second_indirect_blocks(144)))
                i = i + 1
            remaining = blocksNeeded - (144*secondIndirectSets)
            if remaining > 0
                thirdIndirectList.append(secondIndirectList.append(self.fill_second_indirect_blocks(remaining)))
            return thirdIndirectList
        else:
            return thirdIndirectList.append(secondIndirectList.append(self.fill_second_indirect_blocks(blocksNeeded)))
    
    def find_block_prealloc(self):
        '''
        
        '''
        return None
        
    def find_block_no_prealloc(self):
        '''
        
        '''
        return None



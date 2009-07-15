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

    def __init__(self):
        '''
        Constructor
        '''
        self.superBlock = EXT2SuperBlock()
        self.blockGroups = EXT2BlockGroup()
        self.partitionSize = osSettings.partitionSize
        self.blockSize = osSettings.blockSize
        self.nBlockGroups = osSettings.nBlockGroups    #Number of block groups
        self.currentGroup = 0

    def alloc_blocks(self, blocksNeeded):
        '''
        This method fills a list with the blocks
        directly addressed by the file system.
        Usually addresses blocks 1 to 12 (or 0 to 11).
        '''
        i = 1
        directBlocksList = []
        localGroup = self.currentGroup
        while (i<=int(ceil(blocksNeeded/self.superBlock.s_prealloc_blocks))):
            segmentList = []
            segmentList = self.blockGroups[localgroup].find_blocks_prealloc(int(ceil(blocksNeeded/self.superBlock.s_prealloc_blocks)))
            if segmentList == False:
                localGroup = find_group()
                if localGroup != False:
                    segmentList = self.blockGroups[localGroups].find_blocks_no_prealloc(self.superBlock.s_prealloc_blocks)
            i+=1
        remaining = blocksNeeded - (self.superBlock.s_prealloc_blocks*int(ceil(blocksNeeded/self.superBlock.s_prealloc_blocks)))
        if remaining > 0:
            segmentList = []
            segmentList = self.blockGroups[localgroup].find_blocks_prealloc(remaining)
            if segmentList == False:
                    localGroup = find_group()
                    if localGroup != False:
                        self.blockGroups[localGroup].find_blocks_no_prealloc(remaining)
                    else:
                        return False
            directBlocksList.append(segmentList)
        return directBlocksList

    def create_file(self, fileSize):
        '''
        This method creates a file given a file size.
        It search for a group and when available, creates 
        the the inode and its corresponding blocks
        '''
        try:
            inode = blockGroups[currentGroup].create_inode(filesize)
            self.blockGroups[currentGroup].inodeTable[inode.i_inode] = inode
            self.blockGroups[currentGroup].groupDescriptor.bgFreeBlockCount = blockGroups[currentGroup].groupDescriptor.bgFreeBlockCount - 1
            self.blockGroups[currentGroup].groupDescriptor.bgFreeInodesCount = blockGroups[currentGroup].groupDescriptor.bgFreeInodesCount - 1
            self.blockGroups[currentGroup].superBlocks_inodes_count = blockGroups[currentGroup].superBlocks_inodes_count + 1
            self.blockGroups[currentGroup].s_free_inodes_count = blockGroups[currentGroup].s_free_inodes_count + 1
        except:   #Means the partition is full!
            return False

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
        newInode.i_iblock = self.get_blocks(blocksNeeded) #This method should be called by EXT2, not from here
        return newInode

    def delete_file(self, inode):
    #From the inode number, it should be possible to compute its group,
    #go there and delete the inode using the ceil() method.
    #For the moment, the proposed idea would be to use random.choice on the
    #keys of blockGroups to pick a random inode on a random group
        '''
        This method receives the inode number,
        calculates the group it belongs to, and
        deletes it from the file system
        '''        
        return None

    def fill_first_indirect_blocks(self,blocksNeeded):
        '''
        This method fills both the direct and indirect blocks and
        returns a hierarchical list representing the 1st-level redirection
        '''
        firstIndirectList = []
        firstIndirectList.append(self.alloc_blocks(blocksNeeded))
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
                i+=1
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
                i+=1
            remaining = blocksNeeded - (144*secondIndirectSets)
            if remaining > 0
                thirdIndirectList.append(secondIndirectList.append(self.fill_second_indirect_blocks(remaining)))
            return thirdIndirectList
        else:
            return thirdIndirectList.append(secondIndirectList.append(self.fill_second_indirect_blocks(blocksNeeded)))

    def find_group(self, currentGroup):
        '''
        Search the whole file system
        for a block group with free blocks
        '''
        if blockGroups.__len__()==0:  #Means the file system is empty, so start on block group 0
            blockGroups = {0:EXT2BlockGroup()}  #Create the block group 
            currentGroup = 0 
            return True            
        else:
            if blockGroups[currentGroup].groupDescriptor.bgFreeBlocksCount > 0:
                return True
            else:   #The current group is full
                return False

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
            return self.blockGroups[currentGroup].alloc_blocks(blocksNeeded)
        else:
            blocksList = []
            blocksList.append(self.blockGroups[currentGroup].alloc_blocks(blocksNeeded))
            if blocksNeeded > 12 and blocksNeeded <= firstIndirection #1st-Indirection
                blocksList.append(self.blockGroups[currentGroup].fill_first_indirect_blocks(blocksNeeded-12))
                return blocksList
            else:
                if blocksNeeded > firstIndirection and blocksNeeded <= secondIndirection   #2nd-Indirection
                    blocksList.append(self.blockGroups[currentGroup].fill_first_indirect_blocks(blocksNeeded-12))
                    blocksList.append(self.blockGroups[currentGroup].fill_second_indirect_blocks(blocksNeeded - 12 - firstIndirection))
                    return blocksList
                else:
                    if blocksNeeded > secondIndirection and blocksNeeded <= thirdIndirection  #3rd-Indirection
                        blocksList.append(self.blockGroups[currentGroup].fill_first_indirect_blocks(blocksNeeded-12))
                        blocksList.append(self.blockGroups[currentGroup].fill_second_indirect_blocks(blocksNeeded - 12 - firstIndirection))
                        blocksList.append(self.blockGroups[currentGroup].fill_third_indirect_blocks(blocksNeeded - 12 - firstIndirection - secondIndirection))
                        return blocksList
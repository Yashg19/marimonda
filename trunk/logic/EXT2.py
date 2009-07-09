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
        self.blockGroups = {}
        self.partitionSize = osSettings.partitionSize
        self.blockSize = osSettings.blockSize
        self.nBlockGroups = osSettings.nBlockGroups    #Number of block groups
        self.currentGroup = 0
        
    def create_file(self, fileSize):
        '''
        This method creates a file given a file size.
        It search for a group and when available, creates 
        the the inode and its corresponding blocks
        '''
        if self.find_group() == True:
            inode = blockGroups[currentGroup].create_inode(filesize)
            blockGroups[currentGroup].inodeTable[inode.i_inode] = inode
            blockGroups[currentGroup].groupDescriptor.bgFreeBlockCount = blockGroups[currentGroup].groupDescriptor.bgFreeBlockCount - 1
            blockGroups[currentGroup].groupDescriptor.bgFreeInodesCount = blockGroups[currentGroup].groupDescriptor.bgFreeInodesCount - 1
            blockGroups[currentGroup].superBlocks_inodes_count = blockGroups[currentGroup].superBlocks_inodes_count + 1
            blockGroups[currentGroup].s_free_inodes_count = blockGroups[currentGroup].s_free_inodes_count + 1 
        else:   #Means the partition is full!
            pass
        return None

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
        newInode.i_iblock = self.find_blocks(blocksNeeded) #This method should be called by EXT2, not from here
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

    def find_blocks(self,blocksNeeded):
        '''
        This method administer the search of blocks on active block groups.
        It first checks if a group has free blocks and then performs a
        search for blocks supporting preallocation or alternatively, a
        search for the next available block, in case the former case fails.
        If a certain block group has no free blocks, it searches
        on some other group.
        '''
        return None

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
            return self.blockGroups[currentGroup].fill_direct_blocks(blocksNeeded)
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
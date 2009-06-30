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
    currentGroup = 0
    

    def __init__(selfparams):
        '''
        Constructor
        '''
        
    def create_file(self, fileSize):
        '''
        This method creates a file given a file size.
        It search for a group and when available, creates 
        the the inode and its corresponding blocks
        '''
        if find_group() == True:
            inode = blockGroups[currentGroup].create_inode(filesize)
            inode.i_inode = inode.i_inode + currentGroup*osSettings.inodesPerGroup
            blockGroups[currentGroup] = inode
            blockGroups[currentGroup].groupDescriptor.bgFreeBlockCount = blockGroups[currentGroup].groupDescriptor.bgFreeBlockCount - 1
            blockGroups[currentGroup].groupDescriptor.bgFreeInodesCount = blockGroups[currentGroup].groupDescriptor.bgFreeInodesCount - 1
            blockGroups[currentGroup].superBlocks_inodes_count = blockGroups[currentGroup].superBlocks_inodes_count + 1
            blockGroups[currentGroup].s_free_inodes_count = blockGroups[currentGroup].s_free_inodes_count + 1 
        else:   #Means the partition is full!
            pass
        return None
        
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

    def find_group(self, currentGroup):
        '''
        Search the whole file system
        for a block group with free blocks
        '''
        if blockGroups.__len__()==0:  #Means the file system is empty, so start on block group 0
            blockGroups = {0:EXT2BlockGroup()}  #Create the block group 
            currentGroup = 0 #blockGroups[0].find_block()
            return True
            #blockGroups[0].InodeTable[0] = blockGroups[0].create_inode()
            
        else:
            if blockGroups[currentGroup].groupDescriptor.bgFreeBlocksCount > 0:
                return True
            else:   #The current group is full
                return False
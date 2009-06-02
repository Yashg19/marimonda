#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 24/05/2009

@author: yllanos
'''

class EXT2SuperBlock():
    '''
    classdocs
    '''

    s_inodes_count = 0   #Total number of inodes
    s_blocks_count = 0  #Filesystem size in blocks
    s_r_blocks_count = 0  #Number of reserved blocks
    s_free_blocks_count = 0 #Free blocks counter
    s_free_inodes_count = 0 #Free inodes counter
#    s_first_data_block = 0  #Number of first useful block (always 1)
    s_log_block_size = 0  #Block size
#    s_log_frag_size = 0  #Fragment size
    s_blocks_per_group = 0  #Number of blocks per group
#    s_frags_per_group = 0 #Number of fragments per group
    s_inodes_per_group = 0  #Number of inodes per group
#    s_wtime = 0 #Time of last write operation
#    s_def_resuid = 0  #Default UID for reserved blocks
#    s_def_resgid = 0  #Default user group ID for reserved blocks
#    s_first_ino = 0 #Number of first nonreserved inode
#    s_inode_size = 0  #Size of on-disk inode structure
    s_blockgroup_nr = 0 #Block group number of this superblock
    s_prealloc_blocks = 0 #Number of blocks to preallocate
#    s_prealloc_dir_blocks = 0 #Number of blocks to preallocate for directories

    def __init__(selfparams):
        '''
        Constructor
        '''
        
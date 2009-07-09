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


    def __init__(self):
        '''
        Constructor
        '''
        self.s_inodes_count = 0   #Total number of inodes
        self.s_blocks_count = 0  #Filesystem size in blocks
        self.s_r_blocks_count = 0  #Number of reserved blocks
        self.s_free_blocks_count = 0 #Free blocks counter
        self.s_free_inodes_count = 0 #Free inodes counter
    #    self.s_first_data_block = 0  #Number of first useful block (always 1)
        self.s_log_block_size = 0  #Block size
    #    self.s_log_frag_size = 0  #Fragment size
        self.s_blocks_per_group = 0  #Number of blocks per group
    #    self.s_frags_per_group = 0 #Number of fragments per group
        self.s_inodes_per_group = 0  #Number of inodes per group
    #    self.s_wtime = 0 #Time of last write operation
    #    self.s_def_resuid = 0  #Default UID for reserved blocks
    #    self.s_def_resgid = 0  #Default user group ID for reserved blocks
    #    self.s_first_ino = 0 #Number of first nonreserved inode
    #    self.s_inode_size = 0  #Size of on-disk inode structure
        self.s_blockgroup_nr = 0 #Block group number of this superblock
        self.s_prealloc_blocks = 0 #Number of blocks to preallocate
    #    self.s_prealloc_dir_blocks = 0 #Number of blocks to preallocate for directories
        
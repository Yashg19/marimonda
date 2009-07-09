# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 24/05/2009

@author: yllanos
'''

class Inode():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.i_inode = 0
        self.i_isize = 0
        self.i_iblock = []
        # self.i_gid : word;     #User group identifier
        # self.i_uid : word;     #Owner identifier
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 01/06/2009

@author: yllanos
'''


class EXT2GroupDescriptor():
    '''
    This class defines the fields for the group descriptor data structure
    There is only one group descriptor per simulated file system, 
    not one per group
    '''

    bgFreeBlocksCount = None
    bgFreeInodesCount = None    

    def __init__(selfparams):
        '''
        Constructor
        '''
        
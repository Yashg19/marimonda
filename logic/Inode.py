#!/usr/bin/env python
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

    i_inode = 0
    i_isize = 0
    i_iblock = []
    # i_gid : word;     #User group identifier
    # i_uid : word;     #Owner identifier

    def __init__(selfparams):
        '''
        Constructor
        '''
        
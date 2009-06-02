#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 24/05/2009

@author: yllanos
'''

class Filesystem():
    '''
    classdocs
    '''

    maxnFiles = 0   #Maximum number of files supported
    maxVolSize = 0  #Maximum partition Size
    filenameLength = 0 #Maximum number of characters supported for file name
    perm = Permissions() 
    type = ''

    def __init__(selfparams):
        '''
        Constructor
        '''
        
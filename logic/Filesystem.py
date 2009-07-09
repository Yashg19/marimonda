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

    def __init__(self):
        '''
        Constructor
        '''
        self.maxnFiles = 0   #Maximum number of files supported
        self.maxVolSize = 0  #Maximum partition Size
        self.filenameLength = 0 #Maximum number of characters supported for file name
        self.perm = Permissions()
        self.type = ''
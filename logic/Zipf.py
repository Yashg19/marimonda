# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 31/05/2009

@author: yllanos
'''

from Distribution import *

class Zipf(Distribution):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.shape = 1.675
        self.name = 'Zipf'
        
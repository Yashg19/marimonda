# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 31/05/2009

@author: yllanos
'''

from Distribution import *

class Lognormal(Distribution):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.mean = 3.5  #Mean file size
        self.stdDev = 3.5    #Standard deviation
        self.name = 'Lognormal'
        
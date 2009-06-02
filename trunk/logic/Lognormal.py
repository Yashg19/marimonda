#!/usr/bin/env python
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

    mean = 3.5  #Mean file size
    stdDev = 3.5    #Standard deviation
    name = 'Lognormal'

    def __init__(selfparams):
        '''
        Constructor
        '''
        
        
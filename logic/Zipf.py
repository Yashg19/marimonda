#!/usr/bin/env python
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

    shape = 1.675
    name = 'Zipf'

    def __init__(selfparams):
        '''
        Constructor
        '''
        
        
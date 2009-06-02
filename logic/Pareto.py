#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 31/05/2009

@author: yllanos
'''
from Distribution import *

class Pareto(Distribution):
    '''
    classdocs
    '''
    
    shape = 4.5
    name = 'Pareto'

    def __init__(selfparams):
        '''
        Constructor
        '''
        
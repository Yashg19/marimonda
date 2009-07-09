# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 27/05/2009

@author: yllanos
'''


#to further extend the installation to other types of filesystems, 
#please add the modules here
from EXT2 import *

class OSInstaller():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.fsDist = None
        
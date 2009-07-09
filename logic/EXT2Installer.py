# -*- coding: utf-8 -*-
# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 27/05/2009

@author: yllanos
'''

from EXT2InstallerSettings import *
from OSInstaller import *
from scipy import stats
from numpy import random 


class EXT2Installer(OSInstaller):
    '''
    classdocs
    '''



    def __init__(self):
        '''
        Constructor
        '''
        self.filesystem = EXT2()
        self.osSettings = EXT2InstallerSettings()

    def install(self):
        '''
        Installs the EXT2 file system depending 
        on the specified statistical distribution
        '''
        opCounter = 1
        maxSize = osSettings.mean
        aggregateFilesize = 0
        fsSize = 0
        if osSettings.targetDistribution.name == 'Lognormal':
            fsDist = Lognormal()
            install_lognormal()
        if osSettings.targetDistribution.name == 'Pareto':
            fsDist = Pareto()
            install_pareto()
        if osSettings.targetDistribution.name == 'Zipf':
            fsDist = Zipf()
            install_zipf()
        
    def install_lognormal(self):
        '''
        Installs the file system with a Lognormal distribution
        with the specified mean and standard deviation
        '''
        while opCounter<=osSettings.nOperations:
            fileSize = int(random.lognormal(fsDist.mean,fsDist.stdDev))    
            #filesystem.create_file(fileSize)
            if fileSize>maxSize: #TODO: meter aqui la condicion de crear exitosamente el archivo
                maxSize = maxSize
                fsSize = fsSize + fileSize
                opCounter = opCounter +1

    def install_zipf(self):
        '''
        Installs the file system with a Zipf distribution
        with the specified shape
        '''
        while opCounter<=osSettings.nOperations:
            fileSize = int(stats.zipf.rvs(fsDist.shape))    
            #filesystem.create_file(fileSize)
            if fileSize>maxSize: #TODO: meter aqui la condicion de crear exitosamente el archivo
                maxSize = maxSize
                fsSize = fsSize + fileSize
                opCounter = opCounter +1        

    def install_pareto(self):
        '''
        Installs the file system with a Pareto distribution
        whith the specified shape  
        '''
        while opCounter<=osSettings.nOperations:
            fileSize = int(random.pareto(fsDist.shape))    
            #filesystem.create_file(fileSize)
            if fileSize>maxSize: #TODO: meter aqui la condicion de crear exitosamente el archivo
                maxSize = maxSize
                fsSize = fsSize + fileSize
                opCounter = opCounter +1        

#fileSizes = int(random.lognormal(3.5,3.5)) 
        
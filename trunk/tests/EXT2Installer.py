#!/usr/bin/env python
# Copyright (c) 2009, Yamil Jose Llanos Parra. All rights reserved.
'''
Created on 01/06/2009

@author: yllanos
'''
from logic.EXT2Installer import *

test = EXT2Installer()
print test.osSettings.targetDistribution.name
from Pareto import *
test.osSettings.targetDistribution = Pareto()
print test.osSettings.targetDistribution.name
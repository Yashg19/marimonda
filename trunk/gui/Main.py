# Copyright (c) 2009, Yamil José Llanos Parra. All rights reserved.

'''
Created on 25/05/2009

@author: yllanos
'''

from Empty import *

class Main(Empty):
    '''
    classdocs
    '''

    def __init__(self):
        w = gtk.Window()
        w.resize(500,500)
        w.connect('destroy', gtk.main_quit)
        w.show()
        gtk.main()
        

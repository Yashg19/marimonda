'''
Created on 25/05/2009

@author: yllanos
'''

import gtk
import pygtk

class Empty():
    '''
    classdocs
    '''


    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200,200)
        window.connect('destroy', gtk.main_quit)
        #window.show()
        #gtk.main()

    #createWin()    
    #gtk.main()
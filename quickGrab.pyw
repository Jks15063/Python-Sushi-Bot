"""
Assumes screen resolution of 1366x 768,
using chrome browser without bookmarks tool bar enabled.
At top of screen, press down arrow 4 times to center game view.
"""
import pyscreenshot as ImageGrab
import os
import time

#---------------------------
#Global vars
#---------------------------
x_pad = 200
y_pad = 119

def screenGrab():
    #box = (x_pad+1, y_pad+1, x_pad+641, y_pad+481)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()

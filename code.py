"""
Assumes screen resolution of 1366x 768,
using chrome browser without bookmarks tool bar enabled.
Running on linux
At top of screen, press down arrow 4 times to center game view.
"""
import subprocess
import pyscreenshot as ImageGrab
#import Image
import ImageOps
import os
import time
from Xlib import display
#from numpy import *

#---------------------------
#Global vars
#---------------------------
x_pad = 200
y_pad = 119

#foodOnHand
foodOnHand = {'shrim'  : 5,
              'rice'   : 10,
             'nori'   : 10,
              'roe'    : 10,
              'salmon' : 5,
              'unagi'  : 5}

#food_coords
food_coords =   {
    'f_shrimp': { 'X': '241', 'Y': '455'},
    'f_rice':   { 'X': '294', 'Y': '455'},
    'f_nori':   { 'X': '241', 'Y': '510'},
    'f_roe':    { 'X': '294', 'Y': '510'},
    'f_salmon': { 'X': '241', 'Y': '565'},
    'f_unagi':  { 'X': '294', 'Y': '565'},
    'mat':      { 'X': '400', 'Y': '500'}
}

#phone_coords
phone_coords =       {
    'phone':         { 'X': '787', 'Y': '484'},
    'toppings':      { 'X': '738', 'Y': '391'},
    't_shrimp':      { 'X': '692', 'Y': '341'},
    't_nori':        { 'X': '691', 'Y': '397'},
    't_roe':         { 'X': '778', 'Y': '397'},
    't_salmon':      { 'X': '693', 'Y': '453'},
    't_unagi':       { 'X': '773', 'Y': '345'},
    't_exit':        { 'X': '795', 'Y': '458'},
    'menu_rice':     { 'X': '740', 'Y': '416'},
    'buy_rice':      { 'X': '747', 'Y': '402'},
    'delivery_norm': { 'X': '690', 'Y': '415'}
}

#sushiTypes
sushiTypes = {
    1141: 'gunkan',
    1134: 'onigiri',
    1607: 'caliroll'
}

#get seats
#get_seat_one
def get_seat_one():
    box = (227, 181, 227+62, 181+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    b = 0
    for first, second in a:
        b += second
    #print b
    im.save(os.getcwd() + '/seat_one__' + str(int(time.time())) + '.png', "PNG")
    return b

def get_seat_two():
    box = (328, 181, 328+62, 181+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    b = 0
    for first, second in a:
        b += second
    #print b
    im.save(os.getcwd() + '/seat_two__' + str(int(time.time())) + '.png', "PNG")
    return b

def get_seat_three():
    box = (429, 181, 429+62, 181+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    b = 0
    for first, second in a:
        b += second
    #print b
    im.save(os.getcwd() + '/seat_three__' + str(int(time.time())) + '.png', "PNG")
    return b

def get_seat_four():
    box = (530, 181, 530+62, 181+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    b = 0
    for first, second in a:
        b += second
    #print b
    im.save(os.getcwd() + '/seat_four__' + str(int(time.time())) + '.png', "PNG")
    return b

def get_seat_five():
    box = (631, 181, 631+62, 181+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    b = 0
    for first, second in a:
        b += second
    #print b
    im.save(os.getcwd() + '/seat_five__' + str(int(time.time())) + '.png', "PNG")
    return b

def get_seat_six():
    box = (732, 181, 732+62, 181+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    b = 0
    for first, second in a:
        b += second
    #print b
    im.save(os.getcwd() + '/seat_six__' + str(int(time.time())) + '.png', "PNG")
    return b

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

#grab
def grab():
    box = (x_pad+1, y_pad+1, x_pad+641, y_pad+481)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = list(im.getcolors())
    a = a.sum()
    print a
    return a

#screenGrab
def screenGrab():
    #box = (x_pad+1, y_pad+1, x_pad+641, y_pad+481)
    #im = ImageGrab.grab(box)
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

#mousepos
def mousepos():
    data = display.Display().screen().root.query_pointer()._data
    return data['root_x'], data['root_y']

#startGame
def startGame():
    #First menu
    subprocess.call(["xdotool", "mousemove", "511", "327"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.1)

    #Second menu
    subprocess.call(["xdotool", "mousemove", "521", "509"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.1)

    #Third menu
    subprocess.call(["xdotool", "mousemove", "776", "577"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.1)

    #Fourth menu
    subprocess.call(["xdotool", "mousemove", "535", "509"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.1)

#clear_tables
def clear_tables():
    subprocess.call(["xdotool", "mousemove", "280", "330"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.05)

    subprocess.call(["xdotool", "mousemove", "380", "330"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.05)

    subprocess.call(["xdotool", "mousemove", "480", "330"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.05)

    subprocess.call(["xdotool", "mousemove", "580", "330"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.05)

    subprocess.call(["xdotool", "mousemove", "680", "330"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.05)

    subprocess.call(["xdotool", "mousemove", "780", "330"])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(1)

#makeFood
def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        subprocess.call(["xdotool", "mousemove", food_coords['f_rice']['X'], food_coords['f_rice']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_nori']['X'], food_coords['f_nori']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_roe']['X'], food_coords['f_roe']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print 'Making an onigiri'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        subprocess.call(["xdotool", "mousemove", food_coords['f_rice']['X'], food_coords['f_rice']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_rice']['X'], food_coords['f_rice']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_nori']['X'], food_coords['f_nori']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        print 'Making a gunkan'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        subprocess.call(["xdotool", "mousemove", food_coords['f_rice']['X'], food_coords['f_rice']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_nori']['X'], food_coords['f_nori']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_roe']['X'], food_coords['f_roe']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.05)
        subprocess.call(["xdotool", "mousemove", food_coords['f_roe']['X'], food_coords['f_roe']['Y']])
        subprocess.call(["xdotool", "click", "1"])
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

#buyFood
def buyFood(food):
    if food == 'rice':
        subprocess.call(["xdotool", "mousemove", phone_coords['phone']['X'], phone_coords['phone']['Y']])
        time.sleep(.1)
        subprocess.call(["xdotool", "click", "1"])
        subprocess.call(["xdotool", "mousemove", phone_coords['menu_rice']['X'], phone_coords['menu_rice']['Y']])
        time.sleep(.1)
        subprocess.call(["xdotool", "click", "1"])
        s = screenGrab()
        if s.getpixel((747, 402)) != (127, 127, 127):
            print 'rice is available'
            subprocess.call(["xdotool", "mousemove", phone_coords['buy_rice']['X'], phone_coords['buy_rice']['Y']])
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            subprocess.call(["xdotool", "mousemove", phone_coords['delivery_norm']['X'], phone_coords['delivery_norm']['Y']])
            foodOnHand['rice'] += 10
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            time.sleep(2.5)
        else:
            print 'rice is NOT available'
            subprocess.call(["xdotool", "mousemove", phone_coords['t_exit']['X'], phone_coords['t_exit']['Y']])
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        subprocess.call(["xdotool", "mousemove", phone_coords['phone']['X'], phone_coords['phone']['Y']])
        time.sleep(.1)
        subprocess.call(["xdotool", "click", "1"])
        subprocess.call(["xdotool", "mousemove", phone_coords['toppings']['X'], phone_coords['toppings']['Y']])
        time.sleep(.1)
        subprocess.call(["xdotool", "click", "1"])
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel((691, 397)) != (33, 30, 11):
            print 'nori is available'
            subprocess.call(["xdotool", "mousemove", phone_coords['t_nori']['X'], phone_coords['t_nori']['Y']])
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            subprocess.call(["xdotool", "mousemove", phone_coords['delivery_norm']['X'], phone_coords['delivery_norm']['Y']])
            foodOnHand['nori'] += 10
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            time.sleep(2.5)
        else:
            print 'nori is NOT available'
            subprocess.call(["xdotool", "mousemove", phone_coords['t_exit']['X'], phone_coords['t_exit']['Y']])
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        subprocess.call(["xdotool", "mousemove", phone_coords['phone']['X'], phone_coords['phone']['Y']])
        time.sleep(.1)
        subprocess.call(["xdotool", "click", "1"])
        subprocess.call(["xdotool", "mousemove", phone_coords['toppings']['X'], phone_coords['toppings']['Y']])
        time.sleep(.1)
        subprocess.call(["xdotool", "click", "1"])
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel((778, 397)) != (101, 13, 13):
            print 'roe is available'
            subprocess.call(["xdotool", "mousemove", phone_coords['t_roe']['X'], phone_coords['t_roe']['Y']])
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            subprocess.call(["xdotool", "mousemove", phone_coords['delivery_norm']['X'], phone_coords['delivery_norm']['Y']])
            foodOnHand['roe'] += 10
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            time.sleep(2.5)
        else:
            print 'roe is NOT available'
            subprocess.call(["xdotool", "mousemove", phone_coords['t_exit']['X'], phone_coords['t_exit']['Y']])
            time.sleep(.1)
            subprocess.call(["xdotool", "click", "1"])
            time.sleep(1)
            buyFood(food)

#foldMat
def foldMat():
    subprocess.call(["xdotool", "mousemove", food_coords['mat']['X'], food_coords['mat']['Y']])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(.1)

#checkFood
def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j<=4:
                print '%s is low and needs to be replinished' % i
                buyFood(i)

#check_bubs
def check_bubs():
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print 'table 1 is occupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1

    else:
        print "Table 1 unoccupied"

    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print 'table 2 is occupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2

    else:
        print 'Table 2 unoccupied'

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print 'table 3 is occupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3

    else:
        print 'Table 3 unoccupied'

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print 'table 4 is occupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4

    else:
        print 'Table 4 unoccupied'

    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print 'table 5 is occupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5

    else:
        print 'Table 5 unoccupied'

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print 'table 6 is occupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6

    else:
        print 'Table 6 is unoccupied'

    clear_tables()

#main
def main():
    startGame()
    while True:
        check_bubs()

#class Blank
class Blank:
    seat_1 = 7111
    seat_2 = 4978
    seat_3 = 10590
    seat_4 = 9524
    seat_5 = 5589
    seat_6 = 8033

if __name__ == '__main__':
    main()





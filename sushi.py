"""
Bot written in Python for Sushi Go Round Web Games
Link: http://www.miniclip.com/games/sushi-go-round/en/

Test Environment:
OS: Windows 7
Browser: Chrome
Screen Resolution: 1920 x 1080

Note:
Bugs occurred especially after foods on hand insufficient!
"""

import win32api, win32con
import ImageGrab
import os
import time
import ImageOps
from numpy import *

# Global variables
x_pad = 640
y_pad = 154

class Cord:
    f_shrimp = (36,330)
    f_rice = (102,330)
    f_nori = (39,386)
    f_roe = (95,388)
    f_salmon = (38,440)
    f_unagi = (96,442)

    phone = (581,360)

    menu_toppings = (540,269)

    t_shrimp = (500,219)
    t_unagi = (581,229)
    t_nori = (486,280)
    t_roe = (586,282)
    t_salmon = (489,329)
    t_exit = (595,333)

    menu_rice = (508,293)
    buy_rice = (548,282)

    delivery_norm = (494,296)

foodOnHand = {'shrimp':5,
                'rice':10,
                'nori':10,
                'roe':10,
                'salmon':5,
                'unagi':5}

sushiTypes = {2461:'caliroll',
                1824:'gunkan',
                1817:'onigiri'}

blankSeat = {'b_one':6434,
                'b_two':5832,
                'b_three':10536,
                'b_four':10228,
                'b_five':6290,
                'b_six':8689}

def screenGrab():
    box = (x_pad,y_pad,x_pad+639,y_pad+479)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png', 'PNG')
    return im

def grab():
    box = (x_pad,y_pad,x_pad+639,y_pad+479)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click"

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print "Left Down"

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print "Left Up"

def mousePos(cord):
    win32api.SetCursorPos((x_pad+cord[0],y_pad+cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def startGame():
    #location of "PLAY"
    mousePos((326,210))
    leftClick()
    time.sleep(.1)

    #location of "iPHONE"
    mousePos((321,389))
    leftClick()
    time.sleep(.1)

    #location of "SKIP"
    mousePos((578,451))
    leftClick()
    time.sleep(.1)

    #location of "GOAL"
    mousePos((299,380))
    leftClick()
    time.sleep(.1)

def clearTable():
    mousePos((94,206))
    leftClick()

    mousePos((193,207))
    leftClick()

    mousePos((296,209))
    leftClick()

    mousePos((395,207))
    leftClick()

    mousePos((496,207))
    leftClick()

    mousePos((593,210))
    leftClick()

    time.sleep(1)

def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print 'Making a onigiri'
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (109,123,127):
            print 'Rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33,30,11):
            print 'Nori is available'
            mousePos(Cord.t_nori)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (109,123,127):
            print 'Roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print 'Making a onigiri'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan':
        print 'Making a gunkan'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def checkFood():
    for i,j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i =='roe':
            if j <=4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)

def screenShot():
    box = (x_pad,y_pad,x_pad+639,y_pad+479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png', 'PNG')

def get_seat_one():
    firstX = x_pad + 26
    firstY = y_pad + 61
    box = (firstX,firstY,firstX+61,firstY+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_one_' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_two():
    firstX = x_pad + 127
    firstY = y_pad + 61
    box = (firstX,firstY,firstX+61,firstY+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_two_' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    firstX = x_pad + 228
    firstY = y_pad + 61
    box = (firstX,firstY,firstX+61,firstY+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_three_' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    firstX = x_pad + 329
    firstY = y_pad + 61
    box = (firstX,firstY,firstX+61,firstY+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_four_' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    firstX = x_pad + 430
    firstY = y_pad + 61
    box = (firstX,firstY,firstX+61,firstY+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_five_' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    firstX = x_pad + 531
    firstY = y_pad + 61
    box = (firstX,firstY,firstX+61,firstY+14)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\seat_six_' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    screenShot()
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

def check_bubs():
    ### Table 1
    checkFood()
    s1 = get_seat_one()
    if s1 != blankSeat['b_one']:
        if sushiTypes.has_key(s1):
            print 'Table 1 is occupied and needs %s' %sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print 'Sushi not found!\n sushiTypes = %i' %s1
    else:
        print 'Table 1 is unoccupied'

    ### Table 2
    checkFood()
    s2 = get_seat_two()
    if s2 != blankSeat['b_two']:
        if sushiTypes.has_key(s2):
            print 'Table 2 is occupied and needs %s' %sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print 'Sushi not found!\n sushiTypes = %i' %s2
    else:
        print 'Table 2 is unoccupied'

    clearTable()
    ### Table 3
    checkFood()
    s3 = get_seat_three()
    if s3 != blankSeat['b_three']:
        if sushiTypes.has_key(s3):
            print 'Table 3 is occupied and needs %s' %sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print 'Sushi not found!\n sushiTypes = %i' %s3
    else:
        print 'Table 3 is unoccupied'

    ### Table 4
    checkFood()
    s4 = get_seat_four()
    if s4 != blankSeat['b_four']:
        if sushiTypes.has_key(s4):
            print 'Table 4 is occupied and needs %s' %sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print 'Sushi not found!\n sushiTypes = %i' %s4
    else:
        print 'Table 4 is unoccupied'

    clearTable()
    ### Table 5
    checkFood()
    s5 = get_seat_five()
    if s5 != blankSeat['b_five']:
        if sushiTypes.has_key(s5):
            print 'Table 5 is occupied and needs %s' %sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print 'Sushi not found!\n sushiTypes = %i' %s5
    else:
        print 'Table 5 is unoccupied'

    ### Table 6
    checkFood()
    s6 = get_seat_six()
    if s6 != blankSeat['b_six']:
        if sushiTypes.has_key(s6):
            print 'Table 6 is occupied and needs %s' %sushiTypes[s6]
            makeFood(sushiTypes[s5])
        else:
            print 'Sushi not found!\n sushiTypes = %i' %s6
    else:
        print 'Table 6 is unoccupied'

    clearTable()

def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()

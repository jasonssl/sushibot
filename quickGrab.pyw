import ImageGrab
import os
import time

# Global variables
x_pad = 640
y_pad = 154

def screenGrab():
    box = (x_pad,y_pad,x_pad+639,y_pad+479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()

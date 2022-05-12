import RPi.GPIO as GPIO
import threading
import Products
import ReadScanner
import os
import GUI
import time
import web

os.environ['DISPLAY'] = ':0'

clear = lambda: os.system('clear')
items = Products.Products()
remove = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def button1():
    # scan item in
    i = 0
    while(True):
        time.sleep(0.01)
        while(not GPIO.input(21)):
            None
        while(GPIO.input(21)):
            None
        print("{}: Button 1 Pressed".format(i))
        ReadScanner.scan()
        i+=1
    
def button2():
    # remove item by scanning
    i = 0
    global remove
    while(True):
        time.sleep(0.01)
        while(not GPIO.input(20)):
            None
        while(GPIO.input(20)):
            None    
        print("{}: Button 2 Pressed".format(i))
        remove = True
        ReadScanner.scan()
        i+=1

def button3():
    i = 0
    while(True):
        time.sleep(0.01)
        while(not GPIO.input(16)):
            None
        while(GPIO.input(16)):
            None
        print("{}: Button 3 Pressed".format(i))
        w.checkoutScreen()
        web.updateDatabase(items.items)
        w.thankyou()
        time.sleep(1.5)
        items.resetCart()
        clear()
        w.removeWidgets()
        w.refresh(items.items)
        i+=1    


def gui():
    global w
    w = GUI.SmartCartDisplay()
    w.refresh(items.items)
    # w.after(0,w.refresh,items.items)
    try:
        w.mainloop()
    except KeyboardInterrupt:
        w.destroy()
    
if __name__ == '__main__':
    
    t1 = threading.Thread(target=ReadScanner.readData)
    t2 = threading.Thread(target=button1)
    t3 = threading.Thread(target=button2)
    t4 = threading.Thread(target=button3)
    t5 = threading.Thread(target=gui)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    print("Loding complete. Ready to scan.")
    
    containsVals = False
    
    while(True):
        ReadScanner.lock.acquire()
        containsVals = len(ReadScanner.UPC_CODES) > 0
        ReadScanner.lock.release()
        
        if(containsVals):
            ReadScanner.lock.acquire()
            if(remove):
                items.removeItem(ReadScanner.UPC_CODES.pop(0))
                remove = False
            else:
                items.addItem(ReadScanner.UPC_CODES.pop(0))
            containsVals = len(ReadScanner.UPC_CODES) > 0
            ReadScanner.lock.release()
            clear()
            print(items)
            w.refresh(items.items)
    
import threading
import time
import Products
import ReadScanner
import os

clear = lambda: os.system('clear')

if __name__ == '__main__':
    items = Products.Products()
    
    t1 = threading.Thread(target=ReadScanner.readData)
    t1.start()
    print("Loding complete. Ready to scan.")
    
    containsVals = False
    
    while(True):
        ReadScanner.lock.acquire()
        containsVals = len(ReadScanner.UPC_CODES) > 0
        ReadScanner.lock.release()
        
        if(containsVals):
            ReadScanner.lock.acquire()
            items.addItem(ReadScanner.UPC_CODES.pop(0))
            containsVals = len(ReadScanner.UPC_CODES) > 0
            ReadScanner.lock.release()
            clear()
            print(items)
    
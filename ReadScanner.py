import serial
import threading

UPC_CODES = []
lock = threading.Lock()

def readData():
    message = []
    s = serial.Serial('/dev/serial0', timeout=1.5)
    while(s.is_open):
        i = 0
        while(s.in_waiting > 0):
            i = 1
            message.append(s.read_until(' ').decode("utf-8"))
        if(i == 1):
            empty_string = ''
            for val in message:
                empty_string += val
            
            lock.acquire()
            UPC_CODES.append(empty_string)
            lock.release()
            message = []

if __name__ == "__main__":
    readData()

        
    
    
import serial
import threading

UPC_CODES = []
lock = threading.Lock()
s = serial.Serial('/dev/serial0', timeout=0.01)

def readData():
    message = []
    
    while(s.is_open):
        i = 0
        while(s.in_waiting > 0):
            i = 1
            message.append(s.read_until(' '))
        if(i == 1):
            empty_string = ''
            response_code = bytes()
            for val in message:
                empty_string += val.decode("utf-8")
                response_code += val
            
            if(response_code != b'\x02\x00\x00\x01\x0031'):
                lock.acquire()
                UPC_CODES.append(empty_string.replace('\r',''))
                lock.release()
            print(empty_string)
            message = []

def scan():
    packet = bytearray()
    packet.append(0X7E)
    packet.append(0X00)
    packet.append(0X08)
    packet.append(0X01)
    packet.append(0X00)
    packet.append(0X02)
    packet.append(0X01)
    packet.append(0XAB)
    packet.append(0XCD)
    s.write(packet)
    

if __name__ == "__main__":
    readData()

        
    
    
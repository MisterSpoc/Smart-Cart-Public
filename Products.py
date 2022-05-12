import requests
from bs4 import BeautifulSoup as b
import time
import json


class Products:
    """Creates a Products object that contains a dictionary of scanned items and a dictionary of 
    UPC codes to product names
    """
    # static variables
    UPCtoName = {}
    
    def __init__(self):
        self.items = {}
        
        try:
            with open('products.json', 'r') as w:
                data = json.load(w)
                Products.UPCtoName = data
        except:
            print("File probably does not exist")
        
        
        
        
    def __str__(self):
        res = ''
        for key, value in self.items.items():
            res += 'Item: {}, Cost: {}, Quantity: {}\n'.format(key, value[0], value[1])
        return str(res)
    
    
    def addItem(self, UPC):
        """Adds item and price to items dictionary. If item is already in dictionary
        updates quantity. If UPC code has not been scanned before, adds associsation 
        between UPC and item title.

        Args:
            UPC (str): String representation of UPC code
        """
        if(UPC not in Products.UPCtoName.keys()):
            try:
                # search for UPC using internet database
                URL_STRING = "https://www.upcitemdb.com/upc/{}".format(UPC)
                soup = b(requests.get(URL_STRING).text, 'html.parser')
                res = soup.tbody.tr.find_all('td')
                item, price = res[1].string,float(res[2].string.replace("$",""))
            
                Products.UPCtoName[UPC] = item, price
                
                j = json.dumps(Products.UPCtoName)
                with open('products.json','w') as w:
                    w.write(j)
                    
            except:
                print("ERROR: Product not found, please scan again")
                return
        else:
            item, price = Products.UPCtoName[UPC][0], Products.UPCtoName[UPC][1]
            
        if(item not in self.items.keys()):
            self.items[item] = (price, 1)
            # self.items[item]["cost"] = price
            # self.items[item]["quantity"] = 1
        else:
            self.items[item] = (price, self.items[item][1]+1)
            # self.items[item]["cost"] = price
            # self.items[item]["quantity"] = self.items[item]["quantity"] + 1
        return
    
    def removeItem(self, name):
        """Removes item from items dictionary. If quantity is > 1, decrements quantity value by 1

        Args:
            name (str): Name of product to be removed
        """

        if(name in Products.UPCtoName.keys()):
            val = Products.UPCtoName[name][0]
            if(val in self.items.keys()):
                if(self.items[val][1] == 1):
                    self.items.pop(val)
                else:
                    self.items[val] = (self.items[val][0], self.items[val][1]-1)
        return
    
    def resetCart(self):
        self.items.clear()
    
if __name__ == '__main__':
    products = Products()
    products.addItem("041570029701")
    print(products)
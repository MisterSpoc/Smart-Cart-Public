import requests
from bs4 import BeautifulSoup as b


class Products:
    """Creates a Products object that contains a dictionary of scanned items and a dictionary of 
    UPC codes to product names
    """
    # static variables
    UPCtoName = {}
    
    def __init__(self):
        self.items = {}
        
        
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
            
                Products.UPCtoName[UPC] = item
            except:
                print("ERROR: Product not found, please scan again")
                return
        else:
            item, price = Products.UPCtoName[UPC], self.items[Products.UPCtoName[UPC]][0]
            
        if(item not in self.items.keys()):
            self.items[item] = (price, 1)
        else:
            self.items[item] = (price, self.items[item][1]+1)
        return
    
    def removeItem(self, name):
        """Removes item from items dictionary. If quantity is > 1, decrements quantity value by 1

        Args:
            name (str): Name of product to be removed
        """
        if(self.items[name][1] == 1):
            self.items.pop(name)
        else:
            self.items[name] = (self.items[name][0], self.items[name][1]-1)
        return
    
if __name__ == '__main__':
    products = Products()
    products.addItem("041570029701")
    print(products)
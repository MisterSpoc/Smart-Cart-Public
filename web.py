from pymongo import MongoClient


def updateDatabase(items,cart=0,user="likawfy97eyfouwhf"):
    uri = "mongodb+srv://smart-cart.kyqcy.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    try:
        client = MongoClient(uri,
                            tls=True,
                            tlsCertificateKeyFile='X509-cert-3909705342697043999.pem')
        db = client["Smart-Cart"]
        collection = db.carts
        
        new_items = {}
        
        for key,value in items.items():
            new_items[key] = {"price":value[0], "quantity":value[1]}
        
        information = {
            "cart_id":cart,
            "shopper_id":user,
            "receipt":new_items
        }
        
        id = collection.insert_one(information)
        print("Successfully uploaded to database with id:{}".format(id))
    except:
        print("Oops, something went wrong trying to upload to the database")

if __name__ == "__main__":        
    None

class GroceryStore:

    def __init__(self):
        self.l_products=["Pasta","Pizza","Hot-Pocket",
                    "Soup","Russet Potato","Onion","Carrot","Apple","Pineapple"]
        self.d_prices={"Pasta" : 4.50,
                       "Pizza" : 5.75,
                       "Hot-Pocket" : 3.00,
                       "Soup" : 4.50,
                       "Russet Potato" : 0.75,
                       "Onion" : 0.70,
                       "Carrot" : 0.85,
                       "Apple" : 1.50,
                       "Pineapple" : 4.50}
        self.name_store = "Grocery Store"
        self.name_manager = "Joe"
        self.storage={"Pasta" : 10,
                       "Pizza" : 4,
                       "Hot-Pocket" : 7,
                       "Soup" : 5,
                       "Russet Potato" :14,
                       "Onion" : 13,
                       "Carrot" : 20,
                       "Apple" : 21,
                       "Pineapple" : 3}
        

    def get_products(self):
        return(self.l_products)

    def purchase_products(self,l):
        p=[]
        for i in range (len(l)):
            p.append(self.d_prices.get(l[i]))
        total=0
        for i in range(len(p)):
            total=total+p[i]
        return(total)

    def speak_manager(self):
        return ("Hello, my name is Joe. The manager of the Grocery Store.")

    def get_storage(self):
        return(self.storage)
            

def main():
    g=GroceryStore()
    print(g.get_products()) 
    toBuy = []
    storage=g.get_storage()
    while True:
        res = input("What would u like to buy? Type 'stop' if you are done. Or type 'Manager' if you need him.\n")


        if (res!="stop" and res!="Manager"):
            if(storage[res]>0):
                toBuy.append(res)
            storage[res]=storage.get(res)-1
            if (storage[res]<0):
                print("Sorry we ran out of that product")

        if(res=="stop"):
            break
        if(res=="Manager"):
            print(g.speak_manager(),"The loop ended. Please restart if you want to order foods again.")
            break
    if(res!="Manager"):
        print("Here you go!\n you got ", toBuy)
        print("That would be $"+str((g.purchase_products(toBuy)))+" dollars")
'''
    g=GroceryStore()
    cart=[]
    print(g.get_products()) 
    request = input("What food would you like to buy? Please type 'Manager' when you need him.\n")
    if(request=="Manager"):
        print(g.speak_manager())

    elif(request!="Manager"):
        many = int(input("How many would you want?\n"))
        for i in range(many):
            cart.append(request)
        print("Here you go!\n you got " + str(many)+" "+request)
        print("That would be $"+str((g.purchase_products(cart)))+" dollars")
'''
    


if __name__=="__main__":
    main()

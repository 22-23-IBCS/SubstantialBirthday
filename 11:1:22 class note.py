def main():
    food = {"Pasta" : 4.50,
            "Pizza" : 5.75,
            "Hot-Pocket" : 3.00,
            "Soup" : 4.50,
            "Russet Potato":0.75}

    print(list(food.keys()))
    request = input("What food would you like to buy?\n")
    price = food.get(request)
    many = int(input("How many would you want?\n"))
    print("Here you go!\n you got " + str(many)+" "+request)
    print("That would be $"+ str(round(price*many,2))+" dollars")
    

if __name__=="__main__":
    main()

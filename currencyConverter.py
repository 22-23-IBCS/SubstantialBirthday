class Currency_Converter():

    def __init__(self):
        self.countries = ["U.S","Japan","Italy","Mexico","U.K"]
        self.rates = {"Dollar":1,"Yen":132.65,"Euro":0.93,"Peso":19.17,"Pound":0.83}
        self.currency = {"United States":"Dollar",
                    "Japanese":"Yen",
                    "European(Italy)":"Euro",
                    "Mexican":"Peso",
                    "British":"Pound"}

    def getCountry(self):
        return self.countries
    

    def getRates(self):
        return self.rates

    def getCurrency(self):
        return self.currency

    def conversion(self,money,currency1,currency2):
        ratio=self.rates.get(currency1)
        money_in_dollar=float(money)/float(ratio)
        money_in_currency2=money_in_dollar*self.rates.get(currency2)
        return money_in_currency2

def main():

    while True:
        C=Currency_Converter()
        currencyD=C.getCurrency()
        keyCurrency=list(C.currency.keys())
        print("Enter 'Exit' in order to quit\n")
        print("Please enter which type of currency you have. Choose from the list: ")

        for i in range(len(keyCurrency)):
            num=i+1
            print(str(num)+". "+str(keyCurrency[i])+" "+currencyD.get(keyCurrency[i]))

        userInput1 = input("\n")
        if userInput1=="Exit":
            print("Thank you for using the converter")
            break
            

        amount = input("\nPlease enter how much money you have:\n")

        if amount=="Exit":
            print("Thank you for using the converter")
            break

        print("\nPlease enter which type of currency you would like to convert to. Choose from the list:")

        for i in range(len(keyCurrency)):
            num=i+1
            print(str(num)+". "+str(keyCurrency[i])+" "+currencyD.get(keyCurrency[i]))

        
        userInput2 = input("\n")
        if userInput2=="Exit":
            print("Thank you for using the converter")
            break

        print("...calculating...")

        currency1=currencyD.get(keyCurrency[int(userInput1)-1])
        currency2=currencyD.get(keyCurrency[int(userInput2)-1])


        newMoney=C.conversion(amount,currency1,currency2)

        print("\nYou have "+str(newMoney)+" "+currency2+"\n")



if __name__=="__main__":
    main()

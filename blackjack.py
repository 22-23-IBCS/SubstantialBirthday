import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getCard(self):
        return [self.suit, self.name]

class Deck:
    #adds cards to the deck
    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for s in suits:
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)

                C = Card(s, name)
                self.cards.append(C)
    #getter function
    def getCards(self):
        return self.cards

    def dealCard(self):
        newCard = random.choice(self.cards)
        self.cards.remove(newCard)
        return newCard
#adds up all the card values in hand by using forloop. 
def calcHandValue(hand):
    total = 0
    for h in hand:
        name = h[1] #h[1] is the second element of a particular card
        if name == "Ace":
            total = total + 11
            if total > 21:
                total = total - 10
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
        else:
            total = total + int(name)
        
    return total
        

def main():

    print("Welcome to Blackjack!\n") 

    D = Deck()

    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    dealerHand = [D.dealCard().getCard(), D.dealCard().getCard()]

    print("Dealer hand:")
    print(dealerHand[0])
    print("")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    print("")
    
#While loop is used cuz the user should be asked to make decision under a certain condition. "Else:break" is the loop control variable.
    while True:
        option = input("Type 1: Hit  or 2: Stand\n")
        if option == "1":
            userHand.append(D.dealCard().getCard())
            print("")
            print(userHand)
            print("Your hand's value is :" + str(calcHandValue(userHand)))
            print("")

        if option=="2": #This controls the llop by breaking the code if the user doesn't hit
            print("")
            print(userHand)
            print("Your hand's value is :" + str(calcHandValue(userHand)))
            print("")
            if (calcHandValue(dealerHand)>calcHandValue(userHand)):
                print("Dealer hand:")
                print(dealerHand)

                print("deler won")
                break

            if (calcHandValue(dealerHand)<calcHandValue(userHand)):
                print("Dealer hand:")
                print(dealerHand)
                print("user won")
                break

            if (calcHandValue(dealerHand)==calcHandValue(userHand)):
                print("Dealer hand:")
                print(dealerHand)
                print("tie")
                break
        
            break
    

        elif(calcHandValue(userHand)>21):
            print("you're bust. Dealer Won")
            break
        
    if(calcHandValue(userHand)<21):
         print("")
         print("Dealer hand:")
         print(dealerHand)
         print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
         print("")
         print()

#controls the decisoin that dealer makes
    while (calcHandValue(userHand)<21):
        if calcHandValue(dealerHand) < 17:
            print("Dealer hits!\n")
            dealerHand.append(D.dealCard().getCard()) #dealer hand list adds a new random card to it. Might be better to make a new getter function that gets a new card
            print("Dealer hand:")
            print(dealerHand)
            print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))

        
        if(17<calcHandValue(dealerHand)<21):
            dealerHand.append(D.dealCard().getCard())
            print("Dealer hits!\n") #controls the loop by breaking the loop if dealer's hand is above 17, but under 21.
            if (calcHandValue(dealerHand)>calcHandValue(userHand) and calcHandValue(dealerHand)>17):
                print("deler won")
                break

            if (calcHandValue(dealerHand)<calcHandValue(userHand)):
                print("user won")
                break

            if (calcHandValue(dealerHand)==calcHandValue(userHand)):
                print("tie")
                break

        if(calcHandValue(dealerHand)==21):
            if calcHandValue(userHand)!=21:
                print("Dealer wins")
            elif calcHandValue(userHand)==21:
                "tie"
    
        if calcHandValue(dealerHand) > 21: #controls the loop by breaking the loop if the dealer busts
            print("Dealer bust!")
            break
        
        
        
        

if __name__ == "__main__":
    main()

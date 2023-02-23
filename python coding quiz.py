#IBCS Python Coding Quiz
# Name: Junha Yoo

# Read the questions below carefully. Each question describes a
# method that you will need to define with code. In order to demonstrate
# that your method works and test your code, you will need to 'un-comment'
# the method call in the main() method


# 1. Given a list of integers, the method returns True if there are
# at least two numbers in the list that are the maximum values out of
# everything else in the list. If there is only one maximum, the method
# should return false.
import random

def twoMax(l):
    maxi=l[0]
    count=0

    for i in range(len(l)):
        if l[i]>maxi:
            maxi=l[i]
            count=0

        if l[i]==maxi:
            count=count+1

    if count>=2:
        return True
    
    return False


# 2. Given a random integer between 1-15 (inclusive), the method asks
# the user to input an integer between 1-15. If the user's number is
# greater than the random number, the method should print "lower". If
# the user was less than the random number, the method should print "higher".
# If the user got it right, the method should print "You got it!" and stop.
# The user gets to guess 3 times before the method stops otherwise.
def threeGuessGame():
    n=random.randint(1,15)

    for i in range(3):
        a=input("type number between 1-15: ")
        if int(a)>n:
            print("lower")
        if int(a)<n:
            print("higher")
        if int(a)==n:
            print("You got it!")
            break

def main():

    print(twoMax([1, 2, 4, 8, 9, 5, 7, 2, 9, 3]))
    print(twoMax([1, 8, 5, 8, 4, 7, 2, 9, 3]))
    print(twoMax([1, 1, 1, 1]))

    #threeGuessGame()

    
if __name__ == "__main__":
    main()

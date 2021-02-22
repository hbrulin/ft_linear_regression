import sys
import pandas as pd

def get_price(X, theta_0, theta_1) :
    return theta_0 + (theta_1 * X)

def main():
    X_correct = False
    while X_correct == False :
        X_str = input("Enter mileage: ")
        try :
            X = float(X_str) - 0
            if (X >= 0) :
                X_correct = True
            else : 
                print("Mileage is negative")
        except :
            print("Not a number")
    with open('thetas.txt', 'r') as f:
        theta_0, theta_1 = [float(x) for x in next(f).split()]
    estimated_price = get_price(X, theta_0, theta_1)
    print ("Estimated price is: %f" %estimated_price)

if __name__ == "__main__":
    main()
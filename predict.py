import sys
import pandas as pd

def get_price(km, theta_0, theta_1) :
    return theta_0 + (theta_1 * km)

def main():
    km_correct = False
    while km_correct == False :
        km_str = input("Enter mileage: ")
        try :
            km = float(km_str) - 0
            if (km >= 0) :
                km_correct = True
            else : 
                print("Mileage is negative")
        except :
            print("Not a number")
    with open('thetas.txt', 'r') as f:
        theta_0, theta_1 = [float(x) for x in next(f).split()]
    estimated_price = get_price(km, theta_0, theta_1)
    print ("Estimated price is: %f" %estimated_price)

if __name__ == "__main__":
    main()
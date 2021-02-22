import sys
import pandas as pd

def get_Y(X, theta_0, theta_1) :
    return theta_0 + (theta_1 * X)

def main():

    with open('thetas.txt', 'r') as f:
        theta_0, theta_1 = [float(x) for x in next(f).split()]
        nameX, nameY = [str(x) for x in next(f).split()]

    X_correct = False
    while X_correct == False :
        X_str = input("Enter %s: " %nameX)
        try :
            X = float(X_str) - 0
            if (X >= 0) :
                X_correct = True
            else : 
                print("%s is negative" %nameX)
        except :
            print("Not a number")
    estimated_Y = get_Y(X, theta_0, theta_1)
    print ("Estimated %s is: %f" %(nameY, estimated_Y))

if __name__ == "__main__":
    main()
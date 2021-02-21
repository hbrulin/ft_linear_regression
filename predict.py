import sys
import pandas as pd

def get_data(filename) :
    df = pd.read_csv(filename)
    #print(df)
    theta_0 = float(df.iloc[0:len(df),0][0])
    theta_1 = float(df.iloc[0:len(df),0][0])
    return [theta_0, theta_1]

def get_price(km, theta_0, theta_1) :
    return theta_0 + (theta_1 * km)

#error checking
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
    [theta_0, theta_1] = get_data('./thetas.csv')
    estimated_price = get_price(km, theta_0, theta_1)
    print(estimated_price)
    


if __name__ == "__main__":
    main()
import sys
import pandas as pd
from plotter import Plotter

def get_data(dataset) :
    df = pd.read_csv(dataset)
    X = df.iloc[0:len(df),0]#kms
    Y = df.iloc[0:len(df),1]#prices observed
    return [X, Y]

def predict_Y(X, theta_0, theta_1) :
    return theta_0 + (theta_1 * X)

def main():
    #check args for plot
    show_plot = False
    if (len(sys.argv) > 1 and sys.argv[1] == "--plot") :
        show_plot = True

    #open file
    try:
        with open('thetas.txt', 'r') as f:
            theta_0, theta_1 = [float(x) for x in next(f).split()]
            nameX, nameY = [str(x) for x in next(f).split()]
            dataset = [str(x) for x in next(f).split()]
    except:
        sys.exit("Error: Thetas don't exist. Run train.py first.")
    
    #ask for input X
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
    
    #launch predict
    predicted_Y = predict_Y(X, theta_0, theta_1)
    print("Predicted %s is: %f" %(nameY, predicted_Y)) if predicted_Y > 0 else print("0")

    #plot
    if show_plot == True:
        [X_set, Y_set] = get_data(*dataset)
        plotter = Plotter
        plotter.predict_plot(X_set, Y_set, theta_0, theta_1, X, predicted_Y)

if __name__ == "__main__":
    main()
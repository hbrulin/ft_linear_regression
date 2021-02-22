import sys
import pandas as pd
from plotter import Plotter

def get_data(dataset) :
    df = pd.read_csv(dataset)
    X = df.iloc[0:len(df),0]#kms
    Y = df.iloc[0:len(df),1]#prices observed
    return [X, Y]

def predict_Y(X_input, theta_0, theta_1, X_min, X_max) :
    return theta_0 + (theta_1 * X_input)

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
            X_min, X_max = [float(x) for x in next(f).split()]
            dataset = [str(x) for x in next(f).split()]
    except: #for compliance with subject
        print("thetas file doesn't exist. Running with thetas set at 0.")
        theta_0 = theta_1 = 0
        nameX, nameY = "km", "price"
        X_min = X_max = 0
        dataset = ["data.csv"]
    
    #ask for input X
    X_correct = False
    while X_correct == False :
        X_str = input("Enter %s: " %nameX)
        try :
            X_input = float(X_str) - 0
            if (X_input >= 0) :
                X_correct = True
            else : 
                print("%s is negative" %nameX)
        except :
            print("Not a number")

    #scale input
    X_scale = (float(X_input) - X_min) / (X_max - X_min) if X_max else X_input

    #launch predict
    predicted_Y = predict_Y(X_scale, theta_0, theta_1, X_min, X_max)
    print("Predicted %s is: %f" %(nameY, predicted_Y)) if predicted_Y > 0 else print("0")

    #plot
    if show_plot == True:
        [X_set, Y_set] = get_data(*dataset)
        X_set_scale = (X_set.astype(float) - X_min) / (X_max - X_min) if X_max else X_set
        plotter = Plotter
        plotter.predict_plot(X_set_scale, Y_set, theta_0, theta_1, X_scale, predicted_Y)

if __name__ == "__main__":
    main()
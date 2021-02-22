import sys
from utils import Utils
from plotter import Plotter

#global vars
utils = Utils

def predict_Y(X_input, theta_0, theta_1) :
    return theta_0 + (theta_1 * X_input)

def main():
    show_plot = utils.show_plot(sys.argv)
    [thetas, names, X_range, filename] = utils.open()
    
    #ask for input X
    X_correct = False
    while X_correct == False :
        X_str = input("Enter %s: " %names[0])
        try :
            X_input = float(X_str) - 0
            if (X_input >= 0) :
                X_correct = True
            else : 
                print("%s is negative" %names[0])
        except :
            print("Not a number")

    #scale input
    X_scale = utils.scale(X_input, X_range[0], X_range[1]) if X_range[1] else X_input

    #launch predict
    predicted_Y = predict_Y(X_scale, thetas[0], thetas[1])
    print("Predicted %s is: %f" %(names[1], predicted_Y)) if predicted_Y > 0 else print("0")

    #plot
    if show_plot == True:
        [X_set, Y_set, m] = utils.get_data(*filename)
        X_set_scale = utils.scale(X_set, X_range[0], X_range[1]) if X_range[1] else X_set
        plotter = Plotter
        plotter.predict_plot(X_set_scale, Y_set, thetas[0], thetas[1], X_scale, predicted_Y)

if __name__ == "__main__":
    main()
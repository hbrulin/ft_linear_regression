import sys
from utils import Utils
from plotter import Plotter

utils = Utils

def predict_Y(X_input, theta_0, theta_1) :
    return theta_0 + (theta_1 * X_input)

def ask_for_X(names):
    X_correct = False
    while X_correct == False :
        X_str = input("Enter %s: " %names[0])
        try :
            X_input = float(X_str) - 0
            if (X_input >= 0) :
                X_correct = True
            else : 
                print('\33[31m' + "%s is negative" %names[0] + '\33[0m')
        except :
            print('\33[31m' + "Not a number" + '\33[0m')
    return X_input

def main():
    show_plot = utils.show_plot(sys.argv)
    [thetas, names, X_range, filename] = utils.open()
    X_input = ask_for_X(names)
    
    #scale input to same scaling that was used to calculate thetas
    X_scale = utils.scale(X_input, X_range[0], X_range[1]) if X_range[1] else X_input
    #predict
    predicted_Y = predict_Y(X_scale, thetas[0], thetas[1])
    print('\33[32m' + "Predicted %s is: " %names[1] + '\33[0m')
    print('\33[32m' + "%f" %predicted_Y + '\33[0m') if predicted_Y > 0 \
        else print('\33[32m' + "0" + '\33[0m')

    if show_plot == True:
        [X_set, Y_set, m] = utils.get_data(*filename)
        X_set_scale = utils.scale(X_set, X_range[0], X_range[1]) if X_range[1] else X_set
        plotter = Plotter
        plotter.predict_plot(X_set_scale, Y_set, thetas[0], thetas[1], X_scale, predicted_Y)

if __name__ == "__main__":
    main()
import sys

def plot(X, Y, theta_0, theta_1, nameX, nameY):
    plt.scatter(X, Y)
    plt.xlabel(nameX)
    plt.ylabel(nameY)
    function = theta_0 + theta_1 * X
    plt.plot(X, function, color='red')
    plt.savefig('plots/estimate_plot.png')

def predict_Y(X, theta_0, theta_1) :
    return theta_0 + (theta_1 * X)

def main():
    #check args for plot
    show_plot = False
    if (len(sys.argv) > 1 and sys.argv[1] == "--plot") :
        show_plot = True

    #open file
    with open('thetas.txt', 'r') as f:
        theta_0, theta_1 = [float(x) for x in next(f).split()]
        nameX, nameY = [str(x) for x in next(f).split()]
        dataset = [str(x) for x in next(f).split()]
    print(theta_0)
    print(*dataset)
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
    print ("Estimated %s is: %f" %(nameY, predicted_Y))

    #plot
    if show_plot == True:
        plot(X, predicted_Y, theta_0, theta_1, nameX, nameY)

if __name__ == "__main__":
    main()
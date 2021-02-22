import sys
from plotter import Plotter
from utils import Utils

#global vars
learning_rate = 0.1
initial_theta_0 = 0.0
initial_theta_1 = 0.0
utils = Utils

#linear_regression
def calculate_gradiants(old_theta_0, old_theta_1, X, Y, m) :
    theta_0 = 0.0
    theta_1 = 0.0
    for i in range(0, m):
        theta_0 += float(((old_theta_0 + (old_theta_1 * X[i])) - float(Y[i])))
        theta_1 += (((old_theta_0 + (old_theta_1 * X[i]))) - float(Y[i])) * float(X[i])
    theta_0 = (1/m) * theta_0
    theta_1 = (1/m) * theta_1
    return [theta_0, theta_1]

def get_thetas(old_theta_0, old_theta_1, X, Y, m):
    [gradiant_theta_0, gradiant_theta_1] = calculate_gradiants(old_theta_0, old_theta_1, X, Y, m)
    theta_0 = old_theta_0 - (learning_rate * gradiant_theta_0)
    theta_1 = old_theta_1 - (learning_rate * gradiant_theta_1)
    return [theta_0, theta_1]

def train(X, Y, m):
    tmp_theta_0 = initial_theta_0
    tmp_theta_1 = initial_theta_1   
    for i in range(2000):
        [theta_0, theta_1] = get_thetas(tmp_theta_0, tmp_theta_1, X, Y, m)
        tmp_theta_0 = theta_0
        tmp_theta_1 = theta_1
    return [tmp_theta_0, tmp_theta_1]  


def main():
    show_plot = utils.show_plot(sys.argv)

    #getfile
    check_file = False
    while check_file == False :
        filename = input("Enter path to dataset: ")
        try :
            [X, Y, m] = utils.get_data(filename)
            check_file = True
        except :
            print("Error: File does not exist or has wrong format")

    #scale data between 0 & 1 - only needed for X
    X_range = [utils.get_min(X), utils.get_max(X)]
    X_scale = utils.scale(X, X_range[0], X_range[1])

    #launch train
    thetas = train(X_scale, Y, m)
    print ("Results : theta_0: %f, theta_1: %f" %(thetas[0], thetas[1]))

    #save
    names = [X.name, Y.name]
    utils.save(thetas, names, X_range, filename)

    #plot
    if show_plot == True:
        plotter = Plotter
        plotter.train_plot(X_scale, Y, thetas[0], thetas[1])

if __name__ == "__main__":
    main()
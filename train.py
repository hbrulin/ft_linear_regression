import sys
import pandas as pd
from plotter import Plotter

#global vars
learning_rate = 0.1
initial_theta_0 = 0.0
initial_theta_1 = 0.0

#utils
def get_max(data) -> float:
    tmp = 0
    for nb in data:
        if nb > tmp:
            tmp = nb
    return tmp

def get_min(data) -> float:
    tmp = 0
    for nb in data:
        if nb < tmp:
            tmp = nb
    return tmp

def get_data(dataset) :
    df = pd.read_csv(dataset)
    X = df.iloc[0:len(df),0]#kms
    Y = df.iloc[0:len(df),1]#prices observed
    m = len(X)
    return [X, Y, m]

def save(thetas, names, X_range, dataset):
    with open('thetas.txt', 'w') as f:
        f.write("%f %f\n%s %s\n%f %f\n%s" \
            %(thetas[0], thetas[1], names[0], names[1], X_range[0], X_range[1], dataset))

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
    #check args for plot
    show_plot = False
    if (len(sys.argv) > 1 and sys.argv[1] == "--plot") :
        show_plot = True

    #load data
    check_dataset = False
    while check_dataset == False :
        dataset = input("Enter path to dataset: ")
        try :
            [X, Y, m] = get_data(dataset)
            check_dataset = True
        except :
            print("Error: File does not exist or has wrong format")

    #scale to bring data to same range between 0 and 1 - only needed for X
    X_range = [get_min(X), get_max(X)]
    X_scale = (X.astype(float) - X_range[0]) / (X_range[1] - X_range[0])

    #launch train
    thetas = train(X_scale, Y, m)

    #result
    print ("Results : theta_0: %f, theta_1: %f" %(thetas[0], thetas[1]))

    #save
    names = [X.name, Y.name]
    save(thetas, names, X_range, dataset)

    #plot
    if show_plot == True:
        plotter = Plotter
        plotter.train_plot(X_scale, Y, thetas[0], thetas[1])

if __name__ == "__main__":
    main()
import sys
import pandas as pd
import matplotlib.pyplot as plt

#global vars
learning_rate = 0.1
initial_theta_0 = 0.0
initial_theta_1 = 0.0

def get_max(data) -> float:
    tmp = 0
    for nb in data:
        if nb > tmp:
            tmp = nb
    return tmp

def plot(X, Y, theta_0, theta_1):
    plt.scatter(X, Y)
    plt.xlabel(X.name)
    plt.ylabel(Y.name)
    function = theta_0 + theta_1 * X
    plt.plot(X, function, color='red')
    plt.savefig('plots/train_plot.png')

def get_data(filename) :
    df = pd.read_csv(filename)
    X = df.iloc[0:len(df),0]#kms
    Y = df.iloc[0:len(df),1]#prices observed
    m = len(X)
    return [X, Y, m]

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

def save(theta_0, theta_1, nameX, nameY) :
    with open('thetas.txt', 'w') as f:
        f.write("%f %f\n%s %s" %(theta_0, theta_1, nameX, nameY))

def main():
    #check args for plot
    show_plot = False
    if (len(sys.argv) > 1 and sys.argv[1] == "--plot") :
        show_plot = True

    #load data
    check_dataset = False
    while check_dataset == False :
        filename = input("Enter path to dataset: ")
        try :
            [X, Y, m] = get_data(filename)
            check_dataset = True
        except :
            print("Error: File does not exist or has wrong format")

    #normalize to bring data to same range between 0 and 1
    X_norm = [float(X[i])/get_max(X) for i in range(m)]
    Y_norm = [float(Y[i])/get_max(Y) for i in range(m)]

    #launch train
    [theta_0, theta_1] = train(X_norm, Y_norm, m)

    #denormalize
    theta_0 = theta_0 * get_max(Y)
    theta_1 = theta_1 * (get_max(Y) / get_max(X))

    #result
    print ("Results : theta_0: %f, theta_1: %f" %(theta_0, theta_1))

    #save
    save(theta_0, theta_1, X.name, Y.name)

    #plot
    if show_plot == True:
        plot(X, Y, theta_0, theta_1)

if __name__ == "__main__":
    main()
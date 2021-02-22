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

def plot(kms, prices, theta_0, theta_1):
    #print(kms)
    plt.scatter(kms, prices)
    plt.xlabel('Kms')
    plt.ylabel('Prices')
    function = theta_0 + theta_1 * kms
    plt.plot(kms, function, color='red')
    plt.show()

def get_data(filename) :
    df = pd.read_csv(filename)
    kms = df.iloc[0:len(df),0]#kms
    prices = df.iloc[0:len(df),1]#prices observed
    m = len(kms)
    return [kms, prices, m]

def calculate_gradiants(old_theta_0, old_theta_1, kms, prices, m) :
    theta_0 = 0.0
    theta_1 = 0.0
    for i in range(0, m):
        theta_0 += float(((old_theta_0 + (old_theta_1 * kms[i])) - float(prices[i])))
        theta_1 += (((old_theta_0 + (old_theta_1 * kms[i]))) - float(prices[i])) * float(kms[i])
    theta_0 = (1/m) * theta_0
    theta_1 = (1/m) * theta_1
    return [theta_0, theta_1]

def get_thetas(old_theta_0, old_theta_1, kms, prices, m):
    [gradiant_theta_0, gradiant_theta_1] = calculate_gradiants(old_theta_0, old_theta_1, kms, prices, m)
    theta_0 = old_theta_0 - (learning_rate * gradiant_theta_0)
    theta_1 = old_theta_1 - (learning_rate * gradiant_theta_1)
    return [theta_0, theta_1]

def train(kms, prices, m):
    tmp_theta_0 = initial_theta_0
    tmp_theta_1 = initial_theta_1   
    for i in range(2000):
        [theta_0, theta_1] = get_thetas(tmp_theta_0, tmp_theta_1, kms, prices, m)
        tmp_theta_0 = theta_0
        tmp_theta_1 = theta_1
    return [tmp_theta_0, tmp_theta_1]  

def save(theta_0, theta_1) :
    with open('thetas.txt', 'w') as f:
        f.write("%f %f" %(theta_0, theta_1))

def main():
    #check args for plot
    show_plot = False
    if (len(sys.argv) > 2 and sys.argv[1] == "--plot") :
        show_plot = True

    #load data
    check_dataset = False
    while check_dataset == False :
        filename = input("Enter path to dataset: ")
        try :
            [kms, prices, m] = get_data(filename)
            check_dataset = True
        except :
            print("Error: File does not exist or has wrong format")

    #normalize to bring data to same range between 0 and 1
    kms_norm = [float(kms[i])/get_max(kms) for i in range(m)]
    prices_norm = [float(prices[i])/get_max(prices) for i in range(m)]

    #launch train
    [theta_0, theta_1] = train(kms_norm, prices_norm, m)

    #denormalize
    theta_0 = theta_0 * get_max(prices)
    theta_1 = theta_1 * (get_max(prices) / get_max(kms))

    #result
    print ("Results : theta_0: %f, theta_1: %f" %(theta_0, theta_1))

    #save
    save(theta_0, theta_1)

    #plot
    if show_plot == True:
        plot(kms, prices, theta_0, theta_1)

if __name__ == "__main__":
    main()
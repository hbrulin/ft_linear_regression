import sys
import pandas as pd

#global vars
learning_rate = 0.1
initial_theta_0 = 0.0
initial_theta_1 = 0.0

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
    print("gradiant")
    print(theta_0)
    print(theta_1)
    return [theta_0, theta_1]

def get_thetas(old_theta_0, old_theta_1, kms, prices, m):
    [gradiant_theta_0, gradiant_theta_1] = calculate_gradiants(old_theta_0, old_theta_1, kms, prices, m)
    theta_0 = old_theta_0 - (learning_rate * gradiant_theta_0)
    theta_1 = old_theta_1 - (learning_rate * gradiant_theta_1)
    print("get_thetas")
    print(theta_0)
    print(theta_1)
    return [theta_0, theta_1]

def train(kms, prices, m):
    print(initial_theta_0)
    print(initial_theta_1)
    tmp_theta_0 = initial_theta_0
    tmp_theta_1 = initial_theta_1   
    for i in range(2000): #change?
        [theta_0, theta_1] = get_thetas(tmp_theta_0, tmp_theta_1, kms, prices, m)
        tmp_theta_0 = theta_0
        tmp_theta_1 = theta_1
    print("train")
    print(tmp_theta_0)
    print(tmp_theta_1)
    return [tmp_theta_0, tmp_theta_1]  

def save(theta_0, theta_1) :
    f = open("thetas.csv", "w+")
    f.write("theta_1, theta_2\n %f, %f" %(theta_0, theta_1))
    f.close()


#pass file as arg
def main():
    [kms, prices, m] = get_data('data.csv')
    #normalize
    kms_norm = [float(kms[i])/max(kms) for i in range(m)]
    prices_norm = [float(prices[i])/max(prices) for i in range(m)]
    #comments
    [theta_0, theta_1] = train(kms_norm, prices_norm, m)
    #denormalize
    theta_0 = theta_0 * max(prices)
    theta_1 = theta_1 * (max(prices) / max(kms))
    print("main")
    print(theta_0)
    print(theta_1)
    save(theta_0, theta_1)


if __name__ == "__main__":
    main()
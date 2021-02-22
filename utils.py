import pandas as pd
import sys

class Utils:

    def get_data(filename) :
        df = pd.read_csv(filename)
        X = df.iloc[0:len(df),0]#kms
        Y = df.iloc[0:len(df),1]#prices observed
        m = len(X)
        return [X, Y, m]

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

    def scale(to_scale, min, max) :
        try:
            return (to_scale.astype(float) - min) / (max - min)
        except:
            return (float(to_scale) - min) / (max - min)
    
    def save(thetas, names, X_range, filename):
        with open('thetas.txt', 'w') as f:
            f.write("%f %f\n%s %s\n%f %f\n%s" \
                %(thetas[0], thetas[1], names[0], names[1], X_range[0], X_range[1], filename))

    def open():
        try:
            with open('thetas.txt', 'r') as f:
                thetas = [float(x) for x in next(f).split()]
                names = [str(x) for x in next(f).split()]
                X_range = [float(x) for x in next(f).split()]
                filename = [str(x) for x in next(f).split()]
        except: #for compliance with subject
            print('\33[33m' + "Thetas file does not exist. Running with theta coefficients of 0." + '\33[0m')
            thetas = [0, 0]
            names = ["km", "price"]
            X_range = [0, 0]
            filename = ["data.csv"]
            #sys.exit("Error: Thetas file does not exist. Run train.py first.")
        return [thetas, names, X_range, filename]

    def show_plot(args):
        return True if (len(args) > 1 and args[1] == "--plot") else False

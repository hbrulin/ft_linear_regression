import pandas as pd

class Utils:

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

    def get_data(filename) :
        df = pd.read_csv(filename)
        X = df.iloc[0:len(df),0]#kms
        Y = df.iloc[0:len(df),1]#prices observed
        m = len(X)
        return [X, Y, m]

    def save(thetas, names, X_range, dataset):
        with open('thetas.txt', 'w') as f:
            f.write("%f %f\n%s %s\n%f %f\n%s" \
                %(thetas[0], thetas[1], names[0], names[1], X_range[0], X_range[1], dataset))

    def scale(to_scale, min, max) :
        try:
            return (to_scale.astype(float) - min) / (max - min)
        except:
            return (float(to_scale) - min) / (max - min)

    def show_plot(args):
        return True if (len(args) > 1 and args[1] == "--plot") else False
    
    def open():
        try:
            with open('thetas.txt', 'r') as f:
                thetas = [float(x) for x in next(f).split()]
                names = [str(x) for x in next(f).split()]
                X_range = [float(x) for x in next(f).split()]
                filename = [str(x) for x in next(f).split()]
        except: #for compliance with subject
            print("thetas file doesn't exist. Running with thetas set at 0.")
            thetas = [0, 0]
            names = ["km", "price"]
            X_range = [0, 0]
            filename = ["data.csv"]
        return [thetas, names, X_range, filename]

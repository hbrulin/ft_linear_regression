import matplotlib.pyplot as plt

class Plotter:

    def train_plot(X, Y, theta_0, theta_1):
        plt.scatter(X, Y)
        plt.xlabel(X.name)
        plt.ylabel(Y.name)
        function = theta_0 + theta_1 * X
        plt.plot(X, function, color='red')
        plt.savefig('plots/train_plot.png')


    def predict_plot(X, Y, theta_0, theta_1):
        plt.scatter(X, Y)
        plt.xlabel(X.name)
        plt.ylabel(Y.name)
        function = theta_0 + theta_1 * X
        plt.plot(X, function, color='red')
        plt.savefig('plots/predict_plot.png')
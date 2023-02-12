import numpy as np

class LinearRegression:

    #lr= learning rate, n_iters= numbers of iterations
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    
    #X=training samples, y= labels. this method involves training step and gradient descent
    def fit(self, X, y):
        #initialize our parameters
        n_samples, n_features = X.shape
        #assigning zero to weights based on number of features (basically each feature's weight is 0)
        self.weights = np.zeros(n_features)
        self.bias = 0

        #gradient descent; iterative process so we use a for loop
        #for _ in range is because we dnt need to use the variable/index
        for _ in range (self.n_iters):
            #formula for new weights and bias; partial derivatives in respect to each value
            y_predicted = np.dot(X, self.weights) + self.bias
            
            #partial derivative of weights
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))

            #partial derivative of bias
            db = (1/n_samples) * np.sum(y_predicted - y)

            #updated new weights and bias
            self.weights -= self.lr * dw
            self.bias -= self.lr * db 

    #predict method;approximate the value and return it when given new test samples
    def predict(self, X):
        #return y_predicted
        return np.dot(X, self.weights) + self.bias
#K-Nearest Neighbour
import numpy as np
from collections import Counter

#method for calculating euclidean distance btwn 2 feature vectors sqrt root of sum of differences squared
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

class KNN:
    
    #constructor in Python using _init_
    def __init__(self, k=3):
        self.k = k
    
    #method to fit the training samples and training labels
    def fit(self, X, y):
        self.X_train = X
        print("This is X_train")
        print(self.X_train)
        
        self.y_train = y
        print("This is y_train")
        print(self.y_train)

    #method to predict new samples
    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        # compute distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # get k nearest samples, labels, slice up to k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # majority vote, most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

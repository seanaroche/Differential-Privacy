import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import diffprivlib.models as models
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = datasets.load_wine()
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.4)

clf = models.GaussianNB()
clf.fit(X_train, y_train)

epsilons = np.logspace(-2, 2, 50)  
bounds = [(11.03, 14.83), (.74, 5.8), (1.36, 3.23), (10.6, 30), (70, 162), (.98, 3.88), (.34, 5.08), (.13, .66), (.41, 3.58), (1.28, 13), (.48, 1.71), (1.27, 4), (228, 1680)]  #13 tuples, however, content of those min and max from the dataset (wine.data)
accuracy = list()

print(dataset)
for epsilon in epsilons:
    clf = models.GaussianNB(bounds=bounds, epsilon=epsilon)
    clf.fit(X_train, y_train)

    accuracy.append(accuracy_score(y_test, clf.predict(X_test)))

plt.semilogx(epsilons, accuracy)
plt.title("Differentially private Naive Bayes accuracy (Wine Dataset)")
plt.xlabel("epsilon")
plt.ylabel("Accuracy")
plt.show()

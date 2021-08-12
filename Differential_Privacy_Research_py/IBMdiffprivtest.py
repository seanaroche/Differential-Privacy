#Code from IBM Differential privacy library github

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import diffprivlib.models as models
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2)

clf = models.GaussianNB()
clf.fit(X_train, y_train)

print(dataset)  

epsilons = np.logspace(-2, 2, 50)
bounds = [(4.3, 7.9), (2.0, 4.4), (1.1, 6.9), (0.1, 2.5)]
accuracy = list()

for epsilon in epsilons:
    clf = models.GaussianNB(bounds=bounds, epsilon=epsilon)
    clf.fit(X_train, y_train)

    accuracy.append(accuracy_score(y_test, clf.predict(X_test)))

plt.semilogx(epsilons, accuracy)
plt.title("Differentially private Naive Bayes accuracy (Iris Dataset)")
plt.xlabel("epsilon")
plt.ylabel("Accuracy")
plt.show()

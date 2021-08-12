import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
mydataset = pd.read_csv('sampleset.csv')

mydataset = mydataset.drop(columns='ONE')
mydataset = mydataset.drop(columns='TWO')
mydataset = mydataset.drop(columns='THREE')
mydataset = mydataset.drop(columns='FOUR')
mydataset2 = ['Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No']
numyes2 = mydataset2.count('Yes')
numno2 = mydataset2.count('No')
print(numyes2)
print(numno2)

a = 0
for i in mydataset2:
    a = random.randint(0, 100)
    if a > 75:
        if i == 'Yes':
            numyes2 = numyes2 - 1
            numno2 = numno2 + 1
        else:
            numno2 = numno2 - 1
            numyes2 = numyes2 + 1

alteredmyds2 = [numyes2, numno2]

print(alteredmyds2)
bars = ('Yes', 'No')
y_pos = np.arange(len(bars))

plt.bar(y_pos, alteredmyds2, color ='cyan')
plt.xticks(y_pos, bars)
plt.show()


mydataset3 = mydataset2.copy()
mydataset3.extend(mydataset2)
print(mydataset3)
numyes3 = mydataset3.count('Yes')
numno3 = mydataset3.count('No')
print(numyes3)
print(numno3)
for i in mydataset3:
    a = random.randint(0, 100)
    if a > 75:
        if i == 'Yes':
            numyes3 = numyes3 - 1
            numno3 = numno3 + 1
        else:
            numno3 = numno3 - 1
            numyes3 = numyes3 + 1

alteredmyds3 = [numyes3, numno3]

print(alteredmyds3)
bars = ('Yes', 'No')
y_pos = np.arange(len(bars))
plt.bar(y_pos, alteredmyds3)
plt.xticks(y_pos, bars)
plt.show()

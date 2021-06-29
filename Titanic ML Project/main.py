import numpy as np
import pandas as pd
import re

from sklearn.datasets           import load_iris
from sklearn.model_selection    import train_test_split
from sklearn.naive_bayes        import GaussianNB

def clean(data):
    # Filtering Tickets
    for i in range(len(data['Ticket'])):
        data['Ticket'][i] = re.sub('[^0-9]', '', data['Ticket'][i])
        if data['Ticket'][i] != '':
            data['Ticket'][i] = int(data['Ticket'][i])

    # Filtering Cabin
    for i in range(len(data['Cabin'])):
        if data['Cabin'][i] == data['Cabin'][i]:
            data['Cabin'][i] = re.sub('[^A-Z]', '', data['Cabin'][i])

    # Ennumerating Sex, Cabin and Embarkation
    d = {
        'Sex' : {'male' : 0, 'female' : 1},
        'Embarked' : {'S' : 0, 'C' : 1, 'Q' : 2},
        'Cabin' : {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6}
        }

    data = data.replace(d)
    print(data['Survived'])

    return data['Survived'], data.drop(columns={'Survived', 'Name', 'PassengerId'})

# Loading Data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

l1, train = clean(train)
l2, test = clean(test)

model = gaussianNB();

model.fit(train, l1)

predicted = model.predict(test[0])

# TODO: Create Vector
print(predicted)


import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')

d = {
    'Sex' : {'male' : 0, 'female' : 1},
    'Embarked' : {'S' : 0, 'C' : 1, 'Q' : 2}
    }

data['Sex'].map({'male' : 0, 'female' : 1})

print(data['Embarked'])

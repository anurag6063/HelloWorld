import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



dataset = pd.read_csv('../data/Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

print('done', X , ' y ', y)

#Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_geo = LabelEncoder()
X[:, 1] = labelencoder_X_geo.fit_transform(X[:, 1])

labelencoder_X_gen = LabelEncoder()
X[:, 2] = labelencoder_X_gen.fit_transform(X[:, 2])


onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras.wrappers.scikit_learn import KerasClassifier

from sklearn.model_selection import GridSearchCV

from keras.models import Sequential
from keras.layers import Dense

def build_classifier(optimizer):
  classifier = Sequential()
  classifier.add(Dense(input_dim=11, kernel_initializer='uniform', activation='relu', units = 6 ))
  classifier.add(Dense(kernel_initializer='uniform', activation= 'relu', units= 6))
  classifier.add(Dense(kernel_initializer='uniform', activation = 'sigmoid', units = 1))
  classifier.compile(loss = 'binary_crossentropy', optimizer = optimizer, metrics= ['accuracy'] )
  return classifier



classifier = KerasClassifier(build_fn=build_classifier)
parameters = {
    'batch_size' : [25, 30],
    'epochs': [100, 150],
    'optimizer': ['adam', 'rmsprop']
    
    
}


grid_search = GridSearchCV(estimator = classifier, 
                          param_grid = parameters,
                          scoring = 'accuracy',
                          cv=10)




grid_search = grid_search.fit(X_train, y_train)

print ('grid search result', grid_search.best_params_ , ' grid_search.best_score_')
print ('grid search all', grid_search)

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 22:28:04 2023

@author: caich
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor


def print_results(results):
    print('BEST PARAMS: {}\n'.format(results.best_params_))
    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))


DAYS = 10
df = pd.read_csv('archive/stocks/AAP.csv')
df = df.drop('Date', axis=1)
columns = df.columns.to_list()
for col in columns:
    for i in range(1, DAYS + 1):
        df[f'{col}-{i}'] = df[col].shift(i)

df['Prediction'] = df['Adj Close'] > df['Open']

df.drop(['Close', 'Adj Close'], axis=1, inplace=True)
df = df.dropna(how='any')

y = df['Prediction']
sc=StandardScaler()
sc.fit_transform(df)
print(y.value_counts())
print('Base accuracy:', y.value_counts().max() / len(y))
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], y, test_size=0.3, random_state=8)

# clf = SVC()
clf = RandomForestClassifier()
# clf=DecisionTreeClassifier(max_depth=7)
# clf=MLPClassifier()
# clf=GradientBoostingRegressor()
clf.fit(X_train, y_train)
print(clf.score(X_train, y_train))
print(clf.score(X_test, y_test))
print(clf.feature_importances_, X_train.columns)

# parameters={'C': [0.1, 1, 10], 'kernel':['linear','rbf']}
# cv = GridSearchCV(svc, parameters, cv=5)
# cv.fit(X_train, y_train)
# print_results(cv)

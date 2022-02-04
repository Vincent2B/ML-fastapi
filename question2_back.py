from winreg import HKEY_LOCAL_MACHINE
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# My Answer Librairies
from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from fastapi import FastAPI
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split


#############################################################################
#           QUESTION 1 : TRAINING     See Question1.ipynb  for details      #
#############################################################################

def training(new_player):
    # Load dataset
    df = pd.read_csv(".\\nba_logreg.csv")

    # extract names, labels, features names and values
    names = df['Name'].values.tolist() # players names
    labels = df['TARGET_5Yrs'].values # labels
    paramset = df[['GP','PTS','FG%','3P%','OREB']].columns.values
    df_vals = df[['GP','PTS','FG%','3P%','OREB']].values

    # replacing Nan values (only present when no 3 points attempts have been performed by a player)
    for x in np.argwhere(np.isnan(df_vals)):
        df_vals[x]=0.0

    # normalize dataset
    X = MinMaxScaler().fit_transform(df_vals)


    # instanciation du Classifier avec meilleurs hyperparamètres
    clf = tree.DecisionTreeClassifier(max_depth= 5, criterion='gini')
    clf.fit(X, labels)

    result = clf.predict(new_player)

    return result




# Data Preprocessing Python




# FINAL TEMPLATE

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #take all the columns, except the last one
y = dataset.iloc[:, 3].values

#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #remove fit_
"""




# FULL TEMPLATE WITH NOTES

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #take all the columns, except the last one
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encoding Categorial Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Depreciation Warning - The 'categorical_features' keyword is deprecated in version 0.20 and will be removed in 0.22.
# Use Codes Below:
# onehotencoder = OneHotEncoder(categories = 'auto')
# X = np.concatenate((onehotencoder.fit_transform(x[:,0].reshape(-1,1)).toarray(),x[:,1:3]), axis=1)


        #However the "cross_validation" name is now deprecated and was replaced by "model_selection" inside the new anaconda versions.
        #
        #Therefore you might get a warning or even an error if you run this line of code above.
        #
        #To avoid this, you just need to replace:
        #
        #from sklearn.cross_validation import train_test_split 
        #
        #by
        #
        #from sklearn.model_selection import train_test_split 


#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #remove fit_

"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
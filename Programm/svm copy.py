import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
import pickle
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline



dataframe = pd.read_csv(r'C:\testing\yandex.csv')
dataset = dataframe.values

#taking out independent and dependent variable
X = dataset[:,2:]
Y = dataset[:,1:2]



#feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)


#spliting dataset

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.25,random_state = 0)



new_clf = SVC(kernel="poly", degree=2, coef0=1, C=10)
            
# new_clf = SVC(kernel = 'rbf')
new_clf = new_clf.fit(x_train, y_train)
y_pred = new_clf.predict(x_test)
curr_acc = accuracy_score(y_test,y_pred)

print('training accuracy {0}'.format(new_clf.score(x_train, y_train)))
print('testing accuracy {0}'.format(curr_acc))

print(new_clf)



file_name = 'svm_classifier'
outfile = open(file_name,'wb')
pickle.dump(new_clf,outfile)
outfile.close()



ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

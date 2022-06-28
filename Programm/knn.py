import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
import pickle


dataframe = pd.read_csv(r'C:\testing\yandex.csv')
dataset = dataframe.values

#taking out independent and dependent variables
X = dataset[:,2:]
Y = dataset[:,1:2]

#feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

#spliting dataset
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42)

#training model for k = 1,2,3.....25
train_acc_list = []
test_acc_list = []
for neighbour in range(1,26):
    
    clf = KNeighborsClassifier(n_neighbors=neighbour)
    clf = clf.fit(x_train, y_train)
    
    #storing predictions of our model
    y_pred = clf.predict(x_test)
    
    #training accuracy for n neighbour
    train_acc = clf.score(x_train,y_train)
    train_acc_list.append(train_acc)
    
    #testing accuracy for n neighbour
    test_acc = accuracy_score(y_test,y_pred)
    test_acc_list.append(test_acc)
    
#converting it into numpy array
train_acc_list = np.array(train_acc_list) * 100
test_acc_list = np.array(test_acc_list) *100

#plotting training accuracy and testing accuracy
neighbours_list = [i for i in range(1,26)]
plt.plot(train_acc_list, label = 'Training accuracy')
plt.plot(test_acc_list, label = 'Testing accuracy')
plt.xticks()
plt.xlabel('Neighbours')
plt.ylabel('Accuracy %')
plt.legend()
plt.show()

for n in neighbours_list:
    print('Accuracy for n_neighbour = {0} '.format(n))
    print('Training accuracy {0}'.format(train_acc_list[n-1]))
    print('Testing accuracy {0}'.format(test_acc_list[n-1]))
    print('\n')
    

print(clf)
clf = KNeighborsClassifier(n_neighbors=19)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)

print('training accuracy {0}'.format(clf.score(x_train, y_train)))
print('testing accuracy {0}'.format(accuracy_score(y_test,y_pred)))

file_name = 'knn_classifier'
outfile = open(file_name,'wb')
pickle.dump(clf,outfile)
outfile.close()

ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

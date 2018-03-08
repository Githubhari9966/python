from sklearn import datasets
# import data
iris = datasets.load_iris()
X = iris.data[:, :]
y = iris.target

# Splitting the data into the Training data set  and Test data set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 123)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier_linear = SVC(kernel = 'linear', random_state=123)
classifier_linear.fit(X_train, y_train)

# Predicting the Test set results
y_predicted_linear = classifier_linear.predict(X_test)

#Accuracy of linear model
from sklearn.metrics import accuracy_score
print("Accuracy of the model when we use the linear kernel")
print(accuracy_score(y_test, y_predicted_linear))

# Fitting SVM to the Training set
classifier_RBF = SVC(kernel = 'rbf', random_state = 123, gamma = 1.5)
classifier_RBF.fit(X_train, y_train)

# Predicting the Test set results
y_predicted_rbf = classifier_RBF.predict(X_test)

#Accuracy of RBF
print("Accuracy of the model when we are using the RBF kernel")
print(accuracy_score(y_test, y_predicted_rbf))
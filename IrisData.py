from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler
#load dataset
iris=load_iris()
#features and labels
X=iris.data
y=iris.target
#dataset information
print("\n==========IRIS DATA REPORT==========")
print("Total Samples:",len(X))
print("features used:",len(iris.feature_names))
print("Classes :",len(iris.target_names))
print("="*50)
print("\nflower categories:")
 for flower in iris.target_names:
    print("-",flower)
#feature scaling
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
#splitting dataset
X_train, X_test, y_train, y_test=train_test_split(X_scaled, y, test_size=0.2,random_state=42)
#creating model
model=KNeighborsClassifier(n_neighbors=5)
#train model
model.fit(X_train, y_train)
#predict
y_pred=model.predict(X_test)
#accuracy
accuracy=accuracy_score(y_test, y_pred)
print("\n========== MODEL RESULTS ==========")
print("Accuracy:",round(accuracy*100,2),"%")
#confusion matrix
print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))
#classification report
print("\n Classification Report:")
print("="*50)
print(classification_report(y_test,y_pred,target_names=iris.target_names))


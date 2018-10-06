import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor 
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor 

r2_scores=[]
dataset=pd.read_csv('diamonds.csv')
dataset=dataset[(dataset[['x','y','z']] != 0).all(axis=1)]
dataset['volume']=dataset['x']*dataset['y']*dataset['z']
X=dataset.iloc[:,[1,2,3,4,5,6,11]].values
y=dataset.iloc[:,7].values
labelencoder_X1=LabelEncoder()
labelencoder_X2=LabelEncoder()
labelencoder_X3=LabelEncoder()
X[:,1]=labelencoder_X1.fit_transform(X[:,1])
X[:,2]=labelencoder_X2.fit_transform(X[:,2])
X[:,3]=labelencoder_X3.fit_transform(X[:,3])
mask=np.array([[1,2,3]])
onehotencoder_X=OneHotEncoder(categorical_features=mask)
X=onehotencoder_X.fit_transform(X).toarray()
X=X[:,1:27]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3)

#To get the value for R^2 Adjusted
n=X_test.shape[0]
p=X_test.shape[1]

#Linear Regression Model
reg_linear=LinearRegression()
reg_linear.fit(X_train,y_train)
y_pred_linear=reg_linear.predict(X_test)
y_train_linear=reg_linear.predict(X_train)
print('1.Linear Regression')
print('Training Score: ' ,reg_linear.score(X_train,y_train))
print('Testing Score: ',reg_linear.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_linear))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_linear))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_linear)**0.5)
r2_linear=r2_score(y_test, y_pred_linear)
r2_linear=1-(((1-r2_linear)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_linear)
r2_scores.append(r2_linear)

#Support Vector Machine Model
sc_X=StandardScaler()
sc_y=StandardScaler()
X_svr=X
y_svr=y
X_svr=sc_X.fit_transform(X_svr)
y_svr=sc_y.fit_transform(y_svr.reshape(-1,1)).reshape(-1)

X_train_svr,X_test_svr,y_train_svr,y_test_svr=train_test_split(X_svr,y_svr,test_size=.3)
reg_svr=SVR(kernel='rbf')
reg_svr.fit(X_train_svr,y_train_svr)
y_pred_svr=(reg_svr.predict(X_test_svr))
y_jaskaran=sc_y.inverse_transform(y_test_svr)
y_jaskaran_2=sc_y.inverse_transform(y_pred_svr)
print('2.Support Vector Regression("Kernel=RBF")')
print('Training Score : ',reg_svr.score(X_train_svr,y_train_svr))
print('Testing Score: ',reg_svr.score(X_test_svr, y_test_svr))
print('Mean Square Error:',mean_squared_error(y_test_svr, y_pred_svr))
print('Mean Absolute Error:',mean_absolute_error(y_test_svr, y_pred_svr))
print('Root Mean Square Error:',mean_squared_error(y_test_svr, y_pred_svr)**0.5)
r2_svr=r2_score(y_test_svr, y_pred_svr)
r2_svr=1-(((1-r2_svr)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_svr)
r2_scores.append(r2_svr)


#Lasso Linear Regression
reg_lasso = Lasso(normalize=True)
reg_lasso.fit(X_train , y_train)
y_pred_lasso = reg_lasso.predict(X_test)
print('3.Lasso Regression')
print('Training Score : ',reg_lasso.score(X_train,y_train))
print('Testing Score : ',reg_lasso.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_lasso))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_lasso))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_lasso)**0.5)
r2_lasso=r2_score(y_test, y_pred_lasso)
r2_lasso=1-(((1-r2_lasso)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_lasso)
r2_scores.append(r2_lasso)

#Ridge Linear Regression
reg_ridge= Ridge(normalize=True)
reg_ridge.fit(X_train , y_train)
y_pred_ridge = reg_ridge.predict(X_test)
print('4.Ridge Regression')
print('Training Score : ',reg_ridge.score(X_train, y_train))
print('Testing Score : ',reg_ridge.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_ridge))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_ridge))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_ridge)**0.5)
r2_ridge=r2_score(y_test, y_pred_ridge)
r2_ridge=1-(((1-r2_ridge)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_ridge)
r2_scores.append(r2_ridge)

#AdaBoost Regression
reg_ada = AdaBoostRegressor(n_estimators=1000)
reg_ada.fit(X_train , y_train)
y_pred_ada = reg_ada.predict(X_test)
print('5.AdaBoost Regression')
print('Training Score : ',reg_ada.score(X_train, y_train))
print('Testing Score : ',reg_ada.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_ada))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_ada))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_ada)**0.5)
r2_ada=r2_score(y_test, y_pred_ada)
r2_ada=1-(((1-r2_ada)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_ada)
r2_scores.append(r2_ada)

#Gradient Boost Regression
reg_gradient = GradientBoostingRegressor(n_estimators=500, learning_rate=0.1,max_depth=1, random_state=0, loss='ls',verbose = 1)
reg_gradient.fit(X_train , y_train)
y_pred_gradient = reg_gradient.predict(X_test)
print('6.Gradient Boosting Regression')
print('Training Score : ',reg_gradient.score(X_train, y_train))
print('Testing Score : ',reg_gradient.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_gradient))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_gradient))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_gradient)**0.5)
r2_gradient=r2_score(y_test, y_pred_gradient)
r2_gradient=1-(((1-r2_gradient)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_gradient)
r2_scores.append(r2_gradient)

#Random Forest Regression
reg_random = RandomForestRegressor()
reg_random.fit(X_train , y_train)
y_pred_random = reg_random.predict(X_test)
print('7.Random Forest')
print('Training Score : ',reg_random.score(X_train, y_train))
print('Testing Score : ',reg_random.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_random))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_random))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_random)**0.5)
r2_random=r2_score(y_test, y_pred_random)
r2_random=1-(((1-r2_random)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_random)
r2_scores.append(r2_random)

#K-NN Regressor
reg_knn = KNeighborsRegressor()
reg_knn.fit(X_train , y_train)
y_pred_knn = reg_knn.predict(X_test)
print('8.KNeighbours Regression')
print('Training Score: ',reg_knn.score(X_train, y_train))
print('Testing Score : ',reg_knn.score(X_test, y_test))
print('Mean Square Error:',mean_squared_error(y_test, y_pred_knn))
print('Mean Absolute Error:',mean_absolute_error(y_test, y_pred_knn))
print('Root Mean Square Error:',mean_squared_error(y_test, y_pred_knn)**0.5)
r2_knn=r2_score(y_test, y_pred_knn)
r2_knn=1-(((1-r2_knn)*(n-1))/(n-p-1))
print('R2 adjusted:',r2_knn)
r2_scores.append(r2_knn)

#To Store the result for GUI
reg=[reg_linear,reg_svr,reg_lasso,reg_ridge,reg_ada,reg_gradient,reg_random,reg_knn]
reg_encod=[labelencoder_X1,labelencoder_X2,labelencoder_X3,onehotencoder_X]
scaler=[sc_X,sc_y]
file=open('reg.txt','wb')
file2=open('reg_score.txt','wb')
file3=open('reg_encod.txt','wb')
file4=open('reg_scaler.txt','wb')
pickle.dump(reg,file)
pickle.dump(r2_scores,file2)
pickle.dump(reg_encod,file3)
pickle.dump(scaler,file4)
file.close()

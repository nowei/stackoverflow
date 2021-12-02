from sklearn.linear_model import LogisticRegression
LogReg = LogisticRegression(solver = 'lbfgs', multi_class = 'multinomial')
LogReg.fit(newx_train,newy_train[:,0])
ylog_pred = LogReg.predict(newx_test)
print(ylog_pred)
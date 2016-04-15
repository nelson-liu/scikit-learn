from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor()
dt.fit([[1],[2],[3]],[5,6,7], [1,2,1])

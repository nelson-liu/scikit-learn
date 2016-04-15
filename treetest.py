from sklearn import tree

dt = tree.DecisionTreeRegressor()
dt.fit([[1],[2],[3]],[[5,6],[6,7],[7,8]])

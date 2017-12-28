"""
Gender classification  using RandomForestClassifier
  model on scikit

"""

from sklearn.ensemble import RandomForestClassifier

#[hight , wight and shoe size of the people]

result=RandomForestClassifier()

x=[[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

y=Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


#train using given data for making possible classification and prediction 
result=result.fit(x,y)


prediction=clf.predict([[190,70,43]])

print(prediction)

#anwser=male

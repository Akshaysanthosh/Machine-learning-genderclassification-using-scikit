
"""
Gender classification app using scikit-learn

This is a simple program that use scikit libarary to classify gender based on input data 
and make a prediction based on that 
"""

from sklearn import tree

#[hight , wight and shoe size of the people]

x=[[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

y=Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


#train using giben data for making possible classification and prediction 

clf=clf.fit(x,y)


prediction=clf.predict([[190,70,43]])

print(prediction)

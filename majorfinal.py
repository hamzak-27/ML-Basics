# -*- coding: utf-8 -*-
"""majorfinal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NbMxeLrtvGtjvMtJZFWWKcTUGKmrP-HX
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import csv

df = pd.read_table('/content/Restaurant_Reviews.tsv')

df

df.info()

df.describe()

df.columns

df['Liked'].nunique()

print(df['Liked'].unique())

df['Liked'].value_counts()

df.head()

df.tail()

plt.figure(figsize=(8,5))
sns.countplot(x=df.Liked);

x=df['Review'].values
y=df['Liked'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

from sklearn.feature_extraction.text import CountVectorizer
vect =CountVectorizer(stop_words='english')

x_train_vect = vect.fit_transform(x_train)
x_test_vect = vect.transform(x_test)

from sklearn.svm import SVC
model=SVC()

model.fit(x_train_vect,y_train)

y_pred=model.predict(x_test_vect)

accuracy_score(y_pred,y_test)

#####pipeline

# vect = CountVectorizer()
    # tfidf = TfidfTransformer()
    # clf = SGDClassifier()
    # vX = vect.fit_transform(Xtrain)
    # tfidfX = tfidf.fit_transform(vX)
    # predicted = clf.fit_predict(tfidfX)
    # # Now evaluate all steps on test set
    # vX = vect.fit_transform(Xtest)
    # tfidfX = tfidf.fit_transform(vX)
    # predicted = clf.fit_predict(tfidfX)

# pipeline = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
#     ('clf', SGDClassifier()),
# ])
# predicted = pipeline.fit(Xtrain).predict(Xtrain)
# # Now evaluate all steps on test set
# predicted = pipeline.predict(Xtest)

from sklearn.pipeline import make_pipeline
text_model=make_pipeline(CountVectorizer(),SVC())

# pipeline = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
#     ('clf', SGDClassifier()),
# ])
# predicted = pipeline.fit(Xtrain).predict(Xtrain)
# # Now evaluate all steps on test set
# predicted = pipeline.predict(Xtest)

text_model.fit(x_train,y_train)

y_pred=text_model.predict(x_test)

y_pred

accuracy_score(y_pred,y_test)



import joblib
joblib.dump(text_model,'Project')

import joblib
text_model=joblib.load('Project')

text_model.predict(['hello!!Love Your Food'])

text_model.predict(["omg!!it was too spice and i asked you don't add too much "])



df2 = pd.read_csv('/content/Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', df2['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = df2.iloc[:, 1].values



!pip install matplotlib-venn

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB(alpha=0.1)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print ("Confusion Matrix:\n",cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred)
score2 = precision_score(y_test,y_pred)
score3= recall_score(y_test,y_pred)
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

# Bernoulli NB

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import BernoulliNB
classifier = BernoulliNB(alpha=0.8)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print ("Confusion Matrix:\n",cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred)
score2 = precision_score(y_test,y_pred)
score3= recall_score(y_test,y_pred)
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

# Logistic Regression

# Fitting Logistic Regression to the Training set
from sklearn import linear_model
classifier = linear_model.LogisticRegression(C=1.5)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print ("Confusion Matrix:\n",cm)

# Accuracy, Precision and Recall
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
score1 = accuracy_score(y_test,y_pred)
score2 = precision_score(y_test,y_pred)
score3= recall_score(y_test,y_pred)
print("\n")
print("Accuracy is ",round(score1*100,2),"%")
print("Precision is ",round(score2,2))
print("Recall is ",round(score3,2))

"""Using Multinomial Naive Bayes,

Accuracy of prediction is 77.67%.
Precision of prediction is 0.78.
Recall of prediction is 0.77.


Using Bernoulli Naive Bayes,

Accuracy of prediction is 77.0%.
Precision of prediction is 0.76.
Recall of prediction is 0.78.


Using Logistic Regression,

Accuracy of prediction is 76.67%.
Precision of prediction is 0.8.
Recall of prediction is 0.71.

We have learned how to work on support vector classifier and count vectorizer and also we have seen how to use both on the model using pipeline and we have created a model which is able to predict whether the review is positive or negative. We have also seen it using some examples. And we saved the model using the joblib and also retrieved it and used back using the joblib.
"""




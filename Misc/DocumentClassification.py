#!/usr/bin/python
#import pyprind

import pandas as pd
import os

#pbar = pyprind.ProgBar(50000)
#labels = {'pos':1, 'neg':0}

df = pd.DataFrame()

with open("trainingdata.txt", 'r') as infile:
    N = int(infile.readline().strip())
    for line in infile:
        x = line.strip().split()
        y, doc = [int(x[0]), ' '.join(x[1:])]
        df=df.append([[y, doc]], ignore_index=True)
infile.close()

df.columns = ['category', 'document']

# Shuffle data
import numpy as np
np.random.seed(0)
#df = df.reindex(np.random.permutation(df.index))
#df.to_csv('trainingdata.csv')
#df = pd.read_csv('trainingdata.csv')

def shuffle(df, n=1, axis=0):
    df = df.copy()
    for _ in range(n):
        df.apply(np.random.shuffle, axis=axis)
    return df

#df.reset_index(drop=True)




from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer()
# uses a 1-gram by default; change with ngram_range=(2,2)
# Kaanaris, Kanaris, Houvardas, Stamatatos show that a n=3 or 4 is godo for spam filtering
docs = np.array([
    'The sun is shining',
    'The weather is sweet',
    'The sun is shining and the weather is sweet'])
bag = count.fit_transform(docs)

print(count.vocabulary_)
print(bag.toarray())

## Assessing word relevancy via term frequency-inverse document frequency
from sklearn.feature_extraction.text import TfidfTransformer
tfidf = TfidfTransformer()
np.set_printoptions(precision=2)
print(tfidf.fit_transform(count.fit_transform(docs)).toarray())

## Clean text data if needed
## E.g. removing punctuation or html, but maybe keep emoticons?
## df.loc[0, 'document'][-50:] to review
import re
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text
# df['document'] = df['document'].apply(preprocessor)

df['document'] = df['document'].apply(preprocessor)


def tokenizer(text):
    return text.split()
tokenizer('runners like running and thus they run')

from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]
tokenizer_porter('runners like running and thus they run')

## stop-word removal
import nltk
#nltk.download('stopwords')

from nltk.corpus import stopwords
stop = stopwords.words('english')
## [w for w in tokenizer_porter('a runner likes running and runs a lot')[-10:] if w not in stop]

## Training a logistic regression model for document classification

## Divide data into training and testing
q, r = divmod(len(df)/2, 5)  # number of training exmaples to use = 2740 (5485/2 round to nearest multiple of 5)
m = len(df)/2

## Note the slicing behaved unexpectedly due to the reindexing above. This can be fixed by resetting the index or, as above, writing/reading to a file to redefine df

#X_train = df.loc[:m, 'document'].values
#y_train = df.loc[:m, 'category'].values
#X_test = df.loc[m:, 'document'].values
#y_test = df.loc[m:, 'category'].values

X_train = df.iloc[:m, 1].values
y_train = df.iloc[:m, 0].values
X_test = df.iloc[m:, 1].values
y_test = df.iloc[m:, 0].values


## Use GridSearchCV to find optimal set of parameters for logistic regression model using 5-fold statified cross-validation
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)
param_grid = [{'vect__ngram_range': [(1,1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer,
                                   tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1,1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer,
                                   tokenizer_porter],
               'vect__use_idf': [False],
               'vect__norm': [None],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]}
              ]
lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf',
                      LogisticRegression(random_state=0))])
gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='accuracy',
                           cv=5, verbose=1,
                           n_jobs=-1)
model = gs_lr_tfidf.fit(X_train, y_train)
# n_jobs=-1 originally

print('Best parameter set: %s ' % gs_lr_tfidf.best_params_)

## Best parameter set: {'vect__ngram_range': (1, 1),
## 'vect__tokenizer': <function tokenizer_porter at 0x7fa2969cc050>,
## 'clf__penalty': 'l2',
## 'clf__C': 100.0,
## 'vect__stop_words': None}
print('CV Accuracy: %.3f' % gs_lr_tfidf.best_score_)
clf = gs_lr_tfidf.best_estimator_
print('Test Accuracy: %.3f' % clf.score(X_test, y_test))

#https://www.quora.com/Classification-machine-learning-Saving-an-ML-model-in-Python
#http://scikit-learn.org/stable/modules/model_persistence.html
from sklearn.externals import joblib
joblib.dump(model, "DocumentClassification.pkl")

import base64
import pickle as pkl
import zlib
s = base64.encodestring(zlib.compress(pkl.dumps(clf), 9))
print(s)

df['document'] = df['document'].apply(preprocessor)
#df['document'] = df['document'].apply(tokenizer_porter)


#X_train = df.iloc[:m, 1].values
#y_train = df.iloc[:m, 0].values
X_test = df.iloc[m:, 1].values
y_test = df.iloc[m:, 0].values


X_train = df.iloc[:, 1].values
y_train = df.iloc[:, 0].values
X_test = df.iloc[m:, 1].values
y_test = df.iloc[m:, 0].values
`
vectorizer = TfidfVectorizer(strip_accents=None,
                             lowercase=False,
                             preprocessor=None,
                             max_features=2460+15,
                             ngram_range=(1,1),
                             tokenizer=tokenizer_porter,
                             stop_words=None)

X_train = vectorizer.fit_transform(X_train)

lr = LogisticRegression(C=100.0, penalty='l2', random_state=0, n_jobs=-1)
    
model = lr.fit(X_train, y_train)

X_test = vectorizer.fit_transform(X_test)
model.score(X_test, y_test)

# pickle is very large!
# http://stackoverflow.com/questions/17584116/how-to-efficiently-serialize-a-scikit-learn-classifier

s = base64.encodestring(zlib.compress(pkl.dumps(clf), 9))
print(s)

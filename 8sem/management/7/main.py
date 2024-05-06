import re
import pandas as pd
from scipy.sparse import hstack
from sklearn.linear_model import Ridge
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

train = pd.read_csv('./salary-train.csv')
test = pd.read_csv('./salary-test-mini.csv')


for i in range(len(train)):
    train.loc[i, 'FullDescription'] = re.sub('[^a-zA-Z0-9]', ' ', train["FullDescription"].iloc[i].lower())

print(train)
vect = TfidfVectorizer(min_df=5)

x_tr = vect.fit_transform(train['FullDescription'])
train["LocationNormalized"] = train["LocationNormalized"].fillna("nan")
train["ContractTime"] = train["ContractTime"].fillna("nan")

enc = DictVectorizer()
x_train_categ = enc.fit_transform(train[["LocationNormalized", "ContractTime"]].to_dict("records"))
x_test_categ = enc.transform(test[["LocationNormalized", "ContractTime"]].to_dict("records"))
train_feat = hstack([x_tr, x_train_categ])

clf = Ridge(alpha=0.1)
clf.fit(train_feat, train['SalaryNormalized'])

x_test = vect.transform(test['FullDescription'])
test_feat = hstack([x_test, x_test_categ])

y_pred = clf.predict(test_feat)

print(y_pred)


import pandas as pd
fake=pd.read_csv("data/fake.csv")
true=pd.read_csv("data/true.csv")

print("fake News Sample: \n",fake.head())
print("\nTrue News Sample: \n",true.head())

print("\nfake shape: ",fake.shape)
print("true shape: ",true.shape)

# Add label
fake["label"]=0
true["label"]=1

data=pd.concat([fake,true])
data=data.sample(frac=1).reset_index(drop=True)
data=data[["text","label"]]

print("\nmerged data sample: \n",data.head())
print("\nfinal dataset shape: ",data.shape)


import re

def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-z\s]','',text)
    text=re.sub(r'\s+',' ',text)
    return text

data["text"]=data["text"].apply(clean_text)

print("\nCleaned Data Sample: \n",data.head())
    
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer=TfidfVectorizer(max_features=5000)
x=vectorizer.fit_transform(data["text"])
y=data["label"]

print("\nFeature matrix shape:",x.shape)
print("Label shape:",y.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print("\nModel Accuracy:",accuracy)

from sklearn.metrics import classification_report,confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print("\nConfusion Matrix:\n",cm)

report=classification_report(y_test,y_pred)
print("\nClassification Report:\n",report)

import pickle
pickle.dump(model,open("model/model.pkl","wb"))

pickle.dump(vectorizer,open("model/vectorizer.pkl","wb"))

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
    

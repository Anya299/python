import pandas as pd

def load_data():
    data = { 
    "name" : ["john", "anya", "dee", "nandini", None],
    "age" : [None, 15, 28, 39, None]
}

    df = pd.DataFrame(data)
    return df

def clean_data(df):
    df = df.copy()
    df["age"] = df["age"].fillna(df["age"].mean())
    df["name"]=df["name"].fillna("unknown")
    return df

def transform_data(df):
    return df

df = load_data()
df = clean_data(df)
df = transform_data(df)

print(df)

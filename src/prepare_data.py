import pandas as pd

fake = pd.read_csv("data/raw/Fake.csv")
real = pd.read_csv("data/raw/True.csv")

fake["label"] = "FAKE"
real["label"] = "REAL"

data = pd.concat([fake, real])

data = data[["text", "label"]]

data.to_csv("data/news.csv", index=False)

print("Dataset prepared successfully!")
print("Total samples:", len(data))
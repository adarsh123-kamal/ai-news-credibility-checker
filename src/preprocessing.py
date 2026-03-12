import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    
    words = text.split()
    
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)


df = pd.read_csv("data/news.csv")

df["text"] = df["text"].apply(clean_text)

df.to_csv("data/processed_news.csv", index=False)

print("Text preprocessing completed!")
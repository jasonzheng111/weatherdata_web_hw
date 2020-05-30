import pandas as pd

file = "/Users/jason/Documents/GitHub/Web-Challenge/cities.csv"

df = pd.read_csv(file)
df.head()

df.to_html("/Users/jason/Documents/GitHub/Web-Challengecities.html",index=False) 
  

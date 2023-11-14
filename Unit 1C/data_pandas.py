import pandas as pd

data = pd.read_csv("waterloo-data.csv")
print(data.info())

print(data['Name'])
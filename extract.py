import pandas as pd

print("Extract pipeline")

data = {
    "id": [1,2,3],
    "name": ['A', 'B', 'C'],
    "age": [20,24,30]
}
df = pd.DataFrame(data)
print(df)
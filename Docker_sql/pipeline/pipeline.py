import sys
import pandas as pd

print("arguments",sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({"a": [1,2,3], "b":[4,5,6]})
print(df.head())
df["month"] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet", index=False)

print(f"Python executable: {sys.executable}")
print("Hello pipeline!", month)
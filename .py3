import pandas as pd

data = {
    "name": ["Anya", "John", "Dee", "Kiran"],
    "marks": [99, 85, 92, 70]
}

df = pd.DataFrame(data)

# 1. Average marks
avg = df["marks"].mean()

# 2. Top student
top = df.loc[df["marks"].idxmax()]

# 3. Add result column
df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 75 else "Fail")

print("=== REPORT ===")
print(df)
print("\nAverage Marks:", avg)
print("\nTop Student:")
print(top)

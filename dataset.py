import pandas as pd

# Create the dataset
a_values = [round(0.2 * i, 1) for i in range(1, 9)]  # 0.2 to 1.6, step of 0.2
k_values = [2.0] * len(a_values)  # k fixed at 2.0

# Create a DataFrame
df = pd.DataFrame({"a": a_values, "k": k_values})

# Save to CSV
df.to_csv("input_dataset.csv", index=False)
print("Sample dataset 'input_dataset.csv' created successfully.")

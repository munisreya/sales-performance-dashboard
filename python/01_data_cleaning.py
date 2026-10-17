import pandas as pd

# 1. Load the dataset
print("Loading raw data...")
df = pd.read_csv('data/raw/superstore_sales_raw.csv', encoding_errors='ignore')

# 2. Clean up column names (remove hidden spaces)
df.columns = df.columns.str.strip()

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Handle missing values (drop rows missing critical values)
df.dropna(subset=['Sales', 'Profit'], inplace=True)

# 5. Clean currency symbols and convert to float if needed
df['Sales'] = df['Sales'].astype(str).str.replace('$', '').str.replace(',', '').astype(float)
df['Profit'] = df['Profit'].astype(str).str.replace('$', '').str.replace(',', '').astype(float)

# 6. Feature Engineering (Only for available columns)
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# 7. Save the cleaned data
print("\nSaving cleaned data...")
df.to_csv('data/cleaned/superstore_cleaned.csv', index=False)

print(f"\n✅ Done! Cleaned dataset saved with {df.shape[0]} rows and {df.shape[1]} columns.")
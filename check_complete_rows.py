import duckdb
import pandas as pd

# Connect to the DuckDB database
con = duckdb.connect("datasus.db")

# Load the PO (oncology panel) data into pandas DataFrame
query = "SELECT * FROM PO"
df = con.execute(query).fetchdf()

print("Missing values analysis:")
print("=" * 50)

# Count missing values per column
missing_per_column = df.isnull().sum()
print("Missing values per column:")
print(missing_per_column)

print(f"\nTotal rows: {len(df):,}")

# Count rows with NO missing values (all columns filled)
complete_rows = df.dropna()
print(f"Rows with ALL columns filled: {len(complete_rows):,}")

# Calculate percentage
percentage_complete = (len(complete_rows) / len(df)) * 100
print(f"Percentage of complete rows: {percentage_complete:.2f}%")

# Show how many rows have at least one missing value
rows_with_missing = len(df) - len(complete_rows)
print(f"Rows with at least one missing value: {rows_with_missing:,}")

# Close the database connection
con.close()
print("\nDatabase connection closed.") 
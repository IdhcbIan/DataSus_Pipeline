# Step 1: Install the datasus-db package
# Run this only once
# pip install datasus-db

import datasus_db
import duckdb
import pandas as pd

# Step 2: Import the oncology panel data for a specific year
# You can omit `years=[2020]` to download all available years (slower)
datasus_db.import_po(years=[2020])  # This downloads into a DuckDB database file: datasus.db

# Step 3: Connect to the DuckDB database and query into a Pandas DataFrame
con = duckdb.connect("datasus.db")

# Query all rows (or use LIMIT if you want a sample)
query = "SELECT * FROM PO"
df = con.execute(query).fetchdf()  # fetchdf() returns a Pandas DataFrame

# Step 4: Display or use your dataframe
print(df.head())  # Show the first 5 rows

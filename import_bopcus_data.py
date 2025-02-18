import pandas as pd
import mysql.connector
import os

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "A8c-E2g-B1d-W8f+123_MySQL",  # Ensure this is correct
    "database": "bopcus_db"
}

# Full path to the Excel file
excel_file = r"C:\Scripts\Bopcus Project Esme Scott 2025\BOPCUS v3 EASY AID INWARDS.xlsx"

# Check if the file exists
if not os.path.exists(excel_file):
    print(f"❌ Error: File not found at {excel_file}")
    exit()

# Load Excel file
df = pd.read_excel(excel_file, sheet_name=0, dtype=str)

# Debugging: Print actual column names
print("Columns found in Excel file:", df.columns.tolist())

# Select the correct columns (Replace with actual column names from Excel)
df = df[[
    '(i)   BALANCE OF PAYMENTS CATEGORIES APPLICABLE TO BOPCUS – INWARD PAYMENTS',  
    'Unnamed: 1',  
    'Unnamed: 3'  
]]  

# Rename columns to match MySQL table structure
df.columns = ["category_code", "description", "required_documents"]

# Remove leading/trailing spaces
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Replace NaN values with an empty string
df = df.fillna("")

# Remove rows where category_code is empty
df = df[df["category_code"] != ""]

# Remove duplicate category codes
df = df.drop_duplicates(subset=["category_code"])

# Connect to MySQL and insert data
try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Insert Query
    insert_query = """
    INSERT INTO bopcus_categories (category_code, description, required_documents)
    VALUES (%s, %s, %s)
    """

    # Insert each row
    for _, row in df.iterrows():
        cursor.execute(insert_query, (row["category_code"], row["description"], row["required_documents"]))

    # Commit changes
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data imported successfully!")

except mysql.connector.Error as err:
    print(f"❌ Database Error: {err}")

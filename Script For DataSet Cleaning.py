

"""
#  Data Cleaning Scripts for Instacart Datasets

This script contains modular cleaning routines for all key datasets used in the Instacart Market Basket Analysis project. Each section loads, cleans, and saves the respective dataset after applying standard transformations like:
- Lowercasing and trimming string values
- Handling missing values
- Standardizing column names
- Removing duplicates
- Fixing inconsistent naming
- Converting data types

---

## Contents:
- Aisles Dataset
- Departments Dataset
- Orders Dataset
- Order Products (Prior & Train) Dataset

Each block can be reused independently.

---

"""



##### Start of the aisles Cleaning script ######

### aisles Data Set###

import pandas as pd

# Load the dataset



# Load CSV files

file_path = r"E:\Semester 2\Research Proposal\Msc Dissertation\Insta Cart data Set\aisles.csv"
df = pd.read_csv(file_path)

# Strip leading/trailing spaces and convert aisle names to lowercase
df['aisle'] = df['aisle'].str.strip().str.lower()

# Remove duplicate entries (if any)
df = df.drop_duplicates()

# Save cleaned file
cleaned_file_path = "cleaned_aisles.csv"
df.to_csv(cleaned_file_path, index=False)

# Display the cleaned dataframe
import ace_tools as tools # type: ignore
tools.display_dataframe_to_user(name="Cleaned Aisles Data", dataframe=df)

##### End of the aisles Cleaning script ######

##### ------------------#####

##### Start of the Departments Cleaning script ######

### Departments Data Set###

import pandas as pd

# Load the dataset
file_path = r"E:\Semester 2\Research Proposal\Msc Dissertation\Insta Cart data Set\departments.csv"

df = pd.read_csv(file_path)

# Step 1: Inspect the dataset
print("Initial Data Overview:")
print(df.info())  # Check data types and missing values
print("\nUnique Departments Before Cleaning:")
print(df['department'].unique())  # Check unique department names

# Step 2: Check for duplicate rows
duplicate_rows = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_rows}")

# Step 3: Standardize department names
df['department'] = df['department'].str.strip().str.lower()  # Remove extra spaces and convert to lowercase

# Step 4: Correct inconsistent naming
df['department'] = df['department'].replace({
    'meat seafood': 'meat & seafood',  # Standardizing inconsistent names
    'dry goods pasta': 'dry goods & pasta'
})

# Step 5: Save the cleaned dataset
cleaned_file_path = "cleaned_departments.csv"
df.to_csv(cleaned_file_path, index=False)

# Display final dataset overview
print("\nCleaned Data Overview:")
print(df.info())
print("\nUnique Departments After Cleaning:")
print(df['department'].unique())

# Display the cleaned dataset
import ace_tools as tools # type: ignore
tools.display_dataframe_to_user(name="Cleaned Departments Dataset", dataframe=df)

##### End of the Departments Cleaning script ######

##### ------------------#####



##### Start of the orders Cleaning script ######

### orders Data Set###
import pandas as pd

# Load the dataset
file_path = r"E:\Semester 2\Research Proposal\Msc Dissertation\Insta Cart data Set\orders.csv"
df = pd.read_csv(file_path)

# Step 1: Handle Missing Values
# Fill NaN in 'days_since_prior_order' with 0 (assuming first order has no previous order)
df['days_since_prior_order'].fillna(0, inplace=True)

# Step 2: Check for Duplicates and Remove if any
df.drop_duplicates(inplace=True)

# Step 3: Convert Data Types
df = df.astype({
    'order_id': int,
    'user_id': int,
    'order_number': int,
    'order_dow': int,
    'order_hour_of_day': int,
    'days_since_prior_order': int  # Converting to integer since it represents days
})

# Step 4: Standardize Column Names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Save the cleaned dataset to a CSV file
cleaned_file_path = "cleaned_orders.csv"
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning complete. Cleaned dataset saved as 'cleaned_orders.csv'.")


##### End of the orders Cleaning script ######

##### ------------------#####



##### Start of the order_products_prior Cleaning script ######

##### ------------------#####

import pandas as pd

# Define file path
excel_file_path = "E:\Semester 2\Research Proposal\Msc Dissertation\Insta Cart data Set\order_products__prior.csv"

# Load the CSV file
order_products_df = pd.read_csv(excel_file_path)

# Step 1: Handle Missing Values
order_products_df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# Step 2: Remove Duplicates
order_products_df.drop_duplicates(inplace=True)

# Step 3: Convert Data Types (ensure numeric columns are integers)
order_products_df = order_products_df.astype({
    'order_id': int,
    'product_id': int,
    'add_to_cart_order': int,
    'reordered': int
})

# Step 4: Standardize Column Names
order_products_df.columns = order_products_df.columns.str.lower().str.replace(" ", "_")

# Save the cleaned dataset to a new Excel file
cleaned_file_path = "E:\Semester 2\Research Proposal\Msc Dissertation\Insta Cart data Set\cleaned_order_products_prior.csv"
order_products_df.to_csv(cleaned_file_path, index=False)

print("Data cleaning complete. Cleaned dataset saved as 'cleaned_order_products_prior.csv'.")

##### End of the order_products_prior Cleaning script ######

##### ------------------#####



##### Start of the order_products_train Cleaning script ######

##### ------------------#####


# Load the newly uploaded file
file_path = r"E:\Semester 2\Research Proposal\Msc Dissertation\Insta Cart data Set\order_products__train.csv"
train_df = pd.read_csv(file_path)

# Cleaning Steps
# 1. Standardize column names
train_df.columns = train_df.columns.str.lower().str.replace(" ", "_")

# 2. Drop duplicate rows
train_df.drop_duplicates(inplace=True)

# 3. Check and fill missing values (though previous inspection showed none)
train_df.fillna(method='ffill', inplace=True)

# 4. Convert data types (if necessary)
train_df = train_df.astype({
    'order_id': int,
    'product_id': int,
    'add_to_cart_order': int,
    'reordered': int
})

# Save the cleaned dataset
cleaned_file_path = "cleaned_order_products_train.csv"
train_df.to_csv(cleaned_file_path, index=False)

##### End of the order_products_train Cleaning script ######

##### ------------------#####

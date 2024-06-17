import os
import pandas as pd

# Get a list of all CSV files in the working directory
csv_files = [file for file in os.listdir() if file.lower().endswith(".csv")]

# Iterate over each CSV file
for csv_file in csv_files:
    print(f"Processing {csv_file}:")

    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Select the columns of interest (name, value, min, max)
    selected_columns = ["name", "value", "min", "max"]
    df_selected = df[selected_columns]

    # Convert value, min, and max columns to floating point numbers
    df_selected["value"] = df_selected["value"].astype(float)
    df_selected["min"] = df_selected["min"].astype(float)
    df_selected["max"] = df_selected["max"].astype(float)

    # Check if value is within the range (min <= value <= max)
    out_of_range_variables = []
    for index, row in df_selected.iterrows():
        if not (row["min"] <= row["value"] <= row["max"]):
            out_of_range_variables.append(row)

    # Print the variables that are out of range along with their values
    if out_of_range_variables:
        print("The following variables are out of range:")
        for row in out_of_range_variables:
            print(f"Variable: {row['name']}, Value: {row['value']}, Min: {row['min']}, Max: {row['max']}")
    else:
        print("All variables are within the specified range.")
    print("\n")

input("Press Enter to continue...")

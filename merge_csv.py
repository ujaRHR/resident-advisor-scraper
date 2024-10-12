import os
import pandas as pd

folder_path = "outputs"

csv_files = []

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        csv_files.append(df)

merged_csv = pd.concat(csv_files, ignore_index=True)

merged_csv.to_csv("all_events.csv", index=False)

print("All CSV files have been merged into 'all_events.csv'.")
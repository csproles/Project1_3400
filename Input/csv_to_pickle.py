import pandas as pd
import os

# Path to your input CSV file
csv_file_path = 'Input/SpotifyTop100Data.csv'   # adjust if needed
# Desired output path for your Pickle file
pickle_file_path = 'Input/SpotifyTop100Data.pkl'

# Ensure the input file exists
if not os.path.exists(csv_file_path):
    print(f"CSV file not found at: {csv_file_path}")
else:
    # Read CSV and save as Pickle
    df = pd.read_csv(csv_file_path)
    df.to_pickle(pickle_file_path)
    print(f"Spotify data converted to Pickle successfully!\nSaved at: {pickle_file_path}")


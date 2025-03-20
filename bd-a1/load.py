import pandas as pd
import sys

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    file_path = sys.argv[1]
    df = load_data(file_path)
    df.to_csv('titanic_loaded.csv', index=False)
    print("Data loaded successfully!")

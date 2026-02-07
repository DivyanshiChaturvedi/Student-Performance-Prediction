import pandas as pd
import os

def load_data():
    file_path = os.path.join("data", "raw", "StudentsPerformance.csv")
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print(df.shape)

    def load_large_data(path):
        chunks = pd.read_csv(path, chunksize=100000)
        return pd.concat(chunks)



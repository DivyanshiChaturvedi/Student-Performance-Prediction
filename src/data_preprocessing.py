import pandas as pd

def preprocess_data(df):
    # Create target variable
    df["final_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

    # Drop original score columns
    df = df.drop(columns=["math score", "reading score", "writing score"])

    # Convert categorical columns using one-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df

if __name__ == "__main__":
    from data_ingestion import load_data
    df = load_data()
    processed_df = preprocess_data(df)
    print(processed_df.head())


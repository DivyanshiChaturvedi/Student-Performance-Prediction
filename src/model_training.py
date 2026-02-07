from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os

def train_model(df):
    X = df.drop("final_score", axis=1)
    y = df["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/student_model.pkl")

    return mae

if __name__ == "__main__":
    from data_ingestion import load_data
    from data_preprocessing import preprocess_data

    df = load_data()
    df = preprocess_data(df)

    mae = train_model(df)
    print("Model trained successfully")
    print("MAE:", mae)

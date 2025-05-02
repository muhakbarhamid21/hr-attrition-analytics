# import library
import pandas as pd
import joblib

# load model & fitur
model = joblib.load("model/stacking_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")
print("1. Load model & feature columns")

# load data
input_path = "data/employee_data.csv"
df = pd.read_csv(input_path)
print("2. Load data dari ", input_path)

# backup data asli
df_backup = df.copy()
print("3. Backup data asli ke df_backup")

# drop kolom yang tidak relevan
irrelevant_cols = ['EmployeeId', 'EmployeeCount', 'StandardHours', 'Over18']
df = df.drop(columns=[col for col in irrelevant_cols if col in df.columns], errors='ignore')
print("4. Drop kolom yang tidak relevan: ", irrelevant_cols)

# one-hot encoding & reindexing columns
df_encoded = pd.get_dummies(df, drop_first=True)
df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0)
print("5. One-hot encoding & reindexing columns")

# prediksi data
y_pred = model.predict(df_encoded)
y_proba = model.predict_proba(df_encoded)[:, 1]
print("6. Prediksi data")

# simpan hasil prediksi ke df_backup
df_backup['Attrition_Predicted'] = y_pred
df_backup['Attrition_Probability'] = y_proba.round(4)
print("7. Simpan prediksi di df_backup")

# simpan hasil prediksi
output_path = "data/employee_data_predict.csv"
df_backup.to_csv(output_path, index=False)
print(f"8. Simpan hasil prediksi di {output_path}")
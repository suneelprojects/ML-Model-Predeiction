import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample data
data = {
    'ApplicantIncome': [5000, 3000, 4000, 6000, 3500, 4500, 5200, 2700],
    'CreditScore': [700, 650, 600, 720, 580, 690, 710, 640],
    'LoanAmount': [200, 100, 150, 250, 120, 180, 210, 130],
    'Loan_Approved': [1, 0, 0, 1, 0, 1, 1, 0]  # 1 = Approved, 0 = Not Approved
}

df = pd.DataFrame(data)

# Features and target
X = df[['ApplicantIncome', 'CreditScore', 'LoanAmount']]
y = df['Loan_Approved']

# Train/test split (optional here, since small data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
pickle.dump(model, open("loan_model.pkl", "wb"))

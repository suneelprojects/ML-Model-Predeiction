# Loan Approval Prediction App

This is a simple Flask web application that predicts whether a loan application will be approved or rejected based on applicant income, credit score, and loan amount.

The prediction is made using a Random Forest Classifier trained on a small sample dataset.

---

## Features

- Interactive UI with sliders and dropdowns for easy input  
- Real-time input validation  
- Instant prediction results displayed on the webpage  
- Simple REST API endpoint for predictions (`/predict`)

---

## Prerequisites

- Python 3.7 or higher  
- pip package manager

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/suneelprojects/ML-Model-Predeiction.git
   cd ml-loan-approval
2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Train the Model**
   This step creates the loan_model.pkl file.
   ```bash
   python train_loan_model.py
5. **Run the Flask application**
   ```bash
   python loan_app.py
6. **Open your web browser**
   Go to http://localhost:5050 to see the app in action.

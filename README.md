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
   git clone https://github.com/yourusername/ml-loan-approval.git
   cd ml-loan-approval
Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Train the ML model

This step creates the loan_model.pkl file.

bash
Copy
Edit
python train_loan_model.py
Run the Flask application

bash
Copy
Edit
python loan_app.py
Open your web browser

Go to http://localhost:5050 to see the app in action.

Usage
Use the sliders or number inputs to enter:

Applicant Income

Credit Score (choose from dropdown)

Loan Amount

Click Predict to get the loan approval status: Approved or Rejected

API Endpoint
You can also use the /predict endpoint to get predictions programmatically:

URL: /predict

Method: POST

Request JSON body example:

json
Copy
Edit
{
  "features": [5000, 700, 200]
}
Response example:

json
Copy
Edit
{
  "prediction": "Approved"
}
Notes
This is a demo model trained on a very small synthetic dataset, so predictions may not be accurate for real-world data.

To improve accuracy, use a larger dataset and perform proper feature engineering and tuning.

License
MIT License

Feel free to contribute or raise issues!

Developed by [Your Name]

yaml
Copy
Edit

---

You can replace `https://github.com/yourusername/ml-loan-approval.git` and `[Your Name]` with your actual GitHub repo URL and name.

If you want, I can package this as a text file ready to add to your repo!

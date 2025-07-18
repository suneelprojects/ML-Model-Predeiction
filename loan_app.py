from flask import Flask, request, jsonify, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained loan approval model
model = pickle.load(open("loan_model.pkl", "rb"))

# Full HTML with CSS, JS, and validation
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Loan Approval Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
            color: #555;
        }
        input[type=number], select {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 1rem;
        }
        input[type=range] {
            width: 100%;
        }
        button {
            margin-top: 25px;
            width: 100%;
            padding: 12px;
            background: #007bff;
            color: white;
            font-size: 1.1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        button:disabled {
            background: #aaa;
            cursor: not-allowed;
        }
        #result {
            margin-top: 25px;
            font-size: 1.2rem;
            font-weight: bold;
            color: green;
            text-align: center;
        }
        .error {
            color: red;
            font-size: 0.9rem;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h2>Loan Approval Prediction</h2>
    <form id="predictForm" novalidate>
        <label for="income">Applicant Income ($): <span id="incomeVal"></span></label>
        <input type="range" id="income" name="income" min="1000" max="100000" step="1000" value="5000">
        <input type="number" id="incomeNumber" min="1000" max="100000" step="1000" value="5000" required>
        <div id="incomeError" class="error"></div>

        <label for="credit">Credit Score:</label>
        <select id="credit" name="credit" required>
            <option value="">Select Credit Score</option>
            <option value="300">300 - Poor</option>
            <option value="500">500 - Fair</option>
            <option value="650">650 - Good</option>
            <option value="700">700 - Very Good</option>
            <option value="850">850 - Excellent</option>
        </select>
        <div id="creditError" class="error"></div>

        <label for="loan_amount">Loan Amount ($): <span id="loanVal"></span></label>
        <input type="range" id="loan_amount" name="loan_amount" min="1000" max="500000" step="1000" value="20000">
        <input type="number" id="loanNumber" min="1000" max="500000" step="1000" value="20000" required>
        <div id="loanError" class="error"></div>

        <button type="submit" id="submitBtn" disabled>Predict</button>
    </form>
    <div id="result"></div>

<script>
    const incomeSlider = document.getElementById('income');
    const incomeNumber = document.getElementById('incomeNumber');
    const incomeVal = document.getElementById('incomeVal');
    const incomeError = document.getElementById('incomeError');

    const creditSelect = document.getElementById('credit');
    const creditError = document.getElementById('creditError');

    const loanSlider = document.getElementById('loan_amount');
    const loanNumber = document.getElementById('loanNumber');
    const loanVal = document.getElementById('loanVal');
    const loanError = document.getElementById('loanError');

    const submitBtn = document.getElementById('submitBtn');
    const resultDiv = document.getElementById('result');
    const form = document.getElementById('predictForm');

    // Sync sliders and number inputs
    function syncInputs(slider, number) {
        slider.addEventListener('input', () => {
            number.value = slider.value;
            validateForm();
            updateLabels();
        });
        number.addEventListener('input', () => {
            if (number.value < Number(number.min)) number.value = number.min;
            if (number.value > Number(number.max)) number.value = number.max;
            slider.value = number.value;
            validateForm();
            updateLabels();
        });
    }

    syncInputs(incomeSlider, incomeNumber);
    syncInputs(loanSlider, loanNumber);

    // Update label display
    function updateLabels() {
        incomeVal.innerText = incomeNumber.value;
        loanVal.innerText = loanNumber.value;
    }
    updateLabels();

    // Validate form inputs
    function validateForm() {
        let valid = true;

        if (incomeNumber.value === '' || incomeNumber.value < incomeNumber.min || incomeNumber.value > incomeNumber.max) {
            incomeError.textContent = `Income must be between ${incomeNumber.min} and ${incomeNumber.max}`;
            valid = false;
        } else {
            incomeError.textContent = '';
        }

        if (!creditSelect.value) {
            creditError.textContent = 'Please select a credit score';
            valid = false;
        } else {
            creditError.textContent = '';
        }

        if (loanNumber.value === '' || loanNumber.value < loanNumber.min || loanNumber.value > loanNumber.max) {
            loanError.textContent = `Loan amount must be between ${loanNumber.min} and ${loanNumber.max}`;
            valid = false;
        } else {
            loanError.textContent = '';
        }

        submitBtn.disabled = !valid;
    }

    // Initial validation
    validateForm();

    // Form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        submitBtn.disabled = true;
        resultDiv.textContent = "Predicting...";

        const income = parseFloat(incomeNumber.value);
        const credit = parseFloat(creditSelect.value);
        const loan_amount = parseFloat(loanNumber.value);

        try {
            const res = await fetch('/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({features: [income, credit, loan_amount]})
            });

            const data = await res.json();
            resultDiv.textContent = "Loan Approval Status: " + data.prediction;
        } catch (error) {
            resultDiv.textContent = "Error occurred while predicting.";
        }

        submitBtn.disabled = false;
    });
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    pred = model.predict(features)[0]
    status = 'Approved' if pred == 1 else 'Rejected'
    return jsonify({'prediction': status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

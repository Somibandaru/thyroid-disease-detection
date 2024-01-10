from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('hyper_model.pkl')  # Update with the correct filename

@app.route('/')
def home():
    return render_template('home2.html')
@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')

@app.route('/thyfy')
def thyfy():
    return render_template('dfgh2.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        # Extract input values from the form
        features = [float(request.form[f'feature_{i+1}']) for i in range(21)]  # Adjust based on your form field names

        # Convert the input data to a NumPy array
        input_data = np.array(features).reshape(1, -1)
   
        # Make predictions
        prediction = model.predict(input_data)[0]
        if prediction == 0:
            message = "The patient has compensated hypothyroid"
        elif prediction == 1:
            message = "The patient has hyperthyroid"
        elif prediction == 2:
            message = "The patient is healthy without thyroid"
        elif prediction == 3:
            message = "The patient has primary hypothyroid"
        elif prediction == 4:
            message = "The patient has secondary thyroid"
        else:
            message="error"
        
        # Display the prediction
        return render_template('result.html', prediction=prediction,message=message)



if __name__ == '__main__':
    app.run(debug=True)


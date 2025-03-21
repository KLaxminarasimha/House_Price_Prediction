from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            # Retrieve form data
            area = int(request.form.get("area", 0))
            bedrooms = int(request.form.get("bedrooms", 0))
            bathrooms = int(request.form.get("bathrooms", 0))
            stories = int(request.form.get("stories", 0))
            parking = int(request.form.get("parking", 0))
            furnishingstatus = int(request.form.get("furnishingstatus", 0))

            # Handle checkboxes (if unchecked, treat as 0)
            mainroad = int(request.form.get("mainroad", 0))
            guestroom = int(request.form.get("guestroom", 0))
            basement = int(request.form.get("basement", 0))
            hotwaterheating = int(request.form.get("hotwaterheating", 0))
            airconditioning = int(request.form.get("airconditioning", 0))
            prefarea = int(request.form.get("prefarea", 0))

            # Prepare input features
            features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, 
                                  hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])
            
            # Make prediction
            prediction = model.predict(features)[0]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

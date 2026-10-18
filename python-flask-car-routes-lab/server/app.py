from flask import Flask

app = Flask(__name__)

# Sample existing models array for the catalog
existing_models = ["Civic", "Corolla", "Mustang", "Tesla", "BMW"]

# Default root route
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"

# Dynamic route for requesting a specific car model
@app.route("/<model>")
def car_model(model):
    # Check if the model exists in the existing_models array (case-insensitive check is optional, but standard matching uses exact or title case)
    # Here we check against the array directly based on exact match or capitalization if needed.
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == "__main__":
    app.run(debug=True)

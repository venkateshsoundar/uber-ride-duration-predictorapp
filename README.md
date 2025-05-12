# Uber Ride Duration Predictor

A Flask web application that predicts taxi ride durations using a machine learning model trained on historical trip data.

---

## 🚀 Features

- **Ride Duration Prediction**: Input trip details (pickup/dropoff coordinates, passenger count, etc.) to receive predicted ride duration.
- **ML Model**: Pre-trained model loaded from `model.pkl`, trained via `mlmodel.ipynb`.
- **Web Interface**: Simple HTML form built with Flask templates.
- **Training Notebook**: `mlmodel.ipynb` contains the end-to-end model training and evaluation.

---

## 📁 Repository Structure

```
.
├── app.py                # Flask application entrypoint
├── templates/            # HTML templates (index.html, result.html)
├── static/               # Static assets (CSS, JS)
├── mlmodel.ipynb         # Jupyter notebook for training the ML model
├── model.pkl             # Serialized machine learning model
├── taxi.csv              # Taxi trips dataset used for training
├── pyproject.toml        # Poetry dependency configuration
├── poetry.lock           # Locked dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Setup & Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/venkateshsoundar/Uber_ML_App.git
   cd Uber_ML_App
   ```

2. **Install dependencies** (using Poetry)  
   ```bash
   poetry install
   ```

3. **Run the app**  
   ```bash
   poetry run flask run
   ```
   Open your browser at `http://localhost:5000`.

---

## 📚 Model Training

To retrain the model or experiment with different algorithms:

1. Launch Jupyter Notebook:  
   ```bash
   jupyter notebook mlmodel.ipynb
   ```
2. Load `taxi.csv`, preprocess features, train your model, and evaluate metrics.
3. Save the updated model:  
   ```python
   import joblib
   joblib.dump(model, 'model.pkl')
   ```

---

## 🤝 Contributing

1. Fork this repository  
2. Create a branch: `git checkout -b feature/your-feature`  
3. Commit your changes: `git commit -m "Add new feature"`  
4. Push and open a Pull Request

---

## 📜 License

MIT License © 2025 Venkateshwaran B. Soundararajan

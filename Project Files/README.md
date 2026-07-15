# OptiCrop – Smart Agricultural Production Optimization Engine

## Project Overview

OptiCrop is a machine learning powered web application that recommends the
most suitable crop to cultivate based on soil and environmental parameters.
The system analyzes Nitrogen (N), Phosphorous (P), Potassium (K),
Temperature, Humidity, pH, and Rainfall to predict the optimal crop using
a trained classification model.

## Features

- Data preprocessing and cleaning pipeline
- Training and comparison of multiple ML classification models
- Automatic selection of the best performing model
- Model persistence using Pickle (model.pkl, scaler.pkl)
- Flask-based REST/web interface for real-time predictions
- Responsive UI built with HTML5, CSS3, Bootstrap 5, and JavaScript
- Model evaluation reports and confusion matrix visualization

## Technologies

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- HTML5, CSS3, Bootstrap 5
- JavaScript
- Jupyter Notebook
- Pickle (.pkl)

## Installation

```bash
git clone <repository-url>
cd OptiCrop
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
```

## Folder Structure

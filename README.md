# Iris Flower Classification

A beginner-friendly Machine Learning project built using Python and Scikit-learn. The application trains a Decision Tree Classifier on the Iris dataset and predicts the species of a flower based on user-provided measurements.

## Overview

The Iris dataset is one of the most well-known datasets in Machine Learning. It contains measurements of iris flowers belonging to three different species.

This project:

- Loads the Iris dataset
- Splits data into training and testing sets
- Trains a Decision Tree Classifier
- Evaluates model accuracy
- Accepts user input for flower measurements
- Predicts the flower species

## Technologies Used

- Python
- Scikit-learn

## Machine Learning Concepts

- Supervised Learning
- Classification
- Train-Test Split
- Decision Trees
- Model Evaluation
- Accuracy Score

## Project Structure

```text
iris-flower-classification/
│
├── iris_classifier.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/iris-flower-classification.git
```

Navigate to the project folder:

```bash
cd iris-flower-classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

```bash
python iris_classifier.py
```

## Example Input

```text
Sepal Length (in cm): 5.1
Sepal Width (in cm): 3.5
Petal Length (in cm): 1.4
Petal Width (in cm): 0.2
```

## Example Output

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  PREDICTIVE SYSTEM: IRIS SPECIES (96.7% Accuracy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== PREDICTION RESULT ==========
Flower Species: SETOSA
=======================================
```

## Dataset Information

The Iris dataset contains 150 flower samples divided into three classes:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

Features used for prediction:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## How It Works

1. Load the Iris dataset from Scikit-learn.
2. Split the dataset into training and testing sets.
3. Train a Decision Tree Classifier.
4. Evaluate the model using accuracy score.
5. Accept flower measurements from the user.
6. Predict the flower species based on the input.

## Learning Outcomes

Through this project, I learned:

- How to work with datasets in Scikit-learn
- How to split data into training and testing sets
- How to train a Machine Learning model
- How to evaluate model performance
- How to make predictions using user input
- Basic concepts of supervised learning and classification

## Future Improvements

- Add support for multiple ML algorithms
- Compare model performances
- Create a graphical user interface (GUI)
- Visualize the dataset using charts
- Deploy as a web application
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
dataset = load_iris()
features = dataset.data
labels = dataset.target

# Split data into training and testing sets
feat_train, feat_test, label_train, label_test = train_test_split(
    features,
    labels,
    test_size=0.20,
    random_state=101
)

# Create and train the Decision Tree model
dt_classifier = DecisionTreeClassifier(
    criterion="entropy",
    random_state=101
)

dt_classifier.fit(feat_train, label_train)

# Evaluate model performance
test_predictions = dt_classifier.predict(feat_test)
score = accuracy_score(label_test, test_predictions)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"  PREDICTIVE SYSTEM: IRIS SPECIES ({score * 100:.1f}% Accuracy)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# User Input
print("\nPlease provide the characteristics of the sample:")

try:
    sl = float(input(" -> Sepal Length (in cm): "))
    sw = float(input(" -> Sepal Width (in cm): "))
    pl = float(input(" -> Petal Length (in cm): "))
    pw = float(input(" -> Petal Width (in cm): "))
except ValueError:
    print("\n[ERROR] Please enter valid numeric values only.")
    exit()

# Prepare input for prediction
sample_input = [[sl, sw, pl, pw]]

# Predict flower species
predicted_index = dt_classifier.predict(sample_input)[0]
detected_species = dataset.target_names[predicted_index]

print("\n========== PREDICTION RESULT ==========")
print(f"Flower Species: {detected_species.upper()}")
print("=======================================")
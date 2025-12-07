from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load built-in dataset
data = load_iris()

X = data.data      # Features (flower measurements)
y = data.target    # Labels (flower type)

# Step 2: Split data into training & testing parts
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Step 3: Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 4: Predict on test data
predictions = model.predict(X_test)

# Step 5: Check accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
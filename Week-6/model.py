import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_grades.csv")

# Features
X = data[['StudyHours','Attendance','PreviousGrade']]

# Target
y = data['FinalGrade']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Model
model = LinearRegression()

model.fit(X_train,y_train)

# Save files
joblib.dump(model,"model.pkl")
joblib.dump(scaler,"scaler.pkl")

print("Model Saved Successfully")
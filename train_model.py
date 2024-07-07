import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Generate some example data
X = np.random.rand(100, 2)  # 100 samples with 2 features

# Define and train the Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(X)

# Save the model
joblib.dump(model, "my_flask_app/isolation_forest_model.pkl")

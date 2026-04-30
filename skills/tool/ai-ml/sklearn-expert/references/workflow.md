# Standard Workflow

## 8.1 ML Pipeline Workflow

```
Phase 1: Data Loading & Exploration
├── Load data (pandas, numpy)
├── Explore shapes, types, missing values
├── Check class balance for classification
└── Identify feature types

Phase 2: Preprocessing
├── Handle missing values
├── Encode categorical variables
├── Scale/normalize numerical features
└── Create feature engineering pipeline

Phase 3: Model Selection
├── Split data (train/test)
├── Try baseline model
├── Evaluate multiple algorithms
└── Select best performer

Phase 4: Hyperparameter Tuning
├── Define search space
├── Choose search method (grid/random)
├── Tune with cross-validation
└── Evaluate on holdout set

Phase 5: Final Evaluation
├── Final metrics on test set
├── Error analysis
└── Feature importance
```

## 8.2 Complete Classification Pipeline

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load and split data
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Identify feature types
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

# Preprocessing
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

# Create pipeline
pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Grid search
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [5, 10, 20],
    'classifier__min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(
    pipe, param_grid, cv=5, scoring='f1_weighted', n_jobs=-1
)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Evaluate
y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred))
```

## 8.3 Regression Pipeline

```python
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Pipeline for regression
pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', Ridge(alpha=1.0))
])

# Hyperparameter tuning
param_grid = {
    'regressor__alpha': [0.001, 0.01, 0.1, 1.0, 10.0],
}

grid_search = GridSearchCV(
    pipe, param_grid, cv=5, scoring='neg_mean_squared_error'
)
grid_search.fit(X_train, y_train)

# Predictions
y_pred = grid_search.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
```

## 8.4 Cross-Validation Workflow

```python
from sklearn.model_selection import (
    cross_val_score, cross_val_predict,
    StratifiedKFold, RepeatedStratifiedKFold
)

# Basic CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

# Repeated CV for more stable estimates
rcv = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=42)
scores = cross_val_score(model, X, y, cv=rcv, scoring='accuracy')

# Get predictions from CV
y_pred_cv = cross_val_predict(model, X, y, cv=cv)
```

## 8.5 Feature Engineering Pipeline

```python
from sklearn.preprocessing import FunctionTransformer
from sklearn.decomposition import PCA

# Custom transformer
def extract_features(df):
    df = df.copy()
    df['date_year'] = df['date'].dt.year
    df['date_month'] = df['date'].dt.month
    df['date_day'] = df['date'].dt.day
    return df[['date_year', 'date_month', 'date_day']]

# Add to pipeline
pipe = Pipeline([
    ('extract', FunctionTransformer(extract_features)),
    ('preprocessor', preprocessor),
    ('pca', PCA(n_components=10)),
    ('classifier', SVC())
])
```

## 8.6 Model Persistence

```python
import joblib

# Save model
joblib.dump(best_model, 'model.pkl')

# Load model
loaded_model = joblib.load('model.pkl')

# Use loaded model
predictions = loaded_model.predict(X_new)
```

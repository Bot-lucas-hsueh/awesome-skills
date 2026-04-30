# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Data leakage in preprocessing | 🔴 High | Use Pipeline, fit only on train |
| 2 | Not stratifying classification splits | 🔴 High | `stratify=y` in train_test_split |
| 3 | Ignoring class imbalance | 🔴 High | Use class_weight or resampling |
| 4 | Overfitting to validation set | 🟡 Medium | Use nested CV for hyperparameter tuning |
| 5 | Not scaling features for distance models | 🔴 High | Scale before SVM, KNN, PCA |
| 6 | Using accuracy for imbalanced data | 🔴 High | Use f1, precision, recall, AUC |
| 7 | Forgetting to set random_state | 🟡 Medium | Set for reproducibility |
| 8 | Not handling missing values | 🔴 High | Impute or drop |
| 9 | Using wrong metric for task | 🟡 Medium | Match metric to business goal |
| 10 | Not checking feature importance | 🟡 Medium | Analyze after model fitting |

## 10.2 Data Leakage Prevention

```python
# BAD: Fit preprocessor on all data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Leaked!
X_train, X_test = train_test_split(X_scaled)  # WRONG

# GOOD: Fit on train only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Transform only

# BEST: Use Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])

pipe.fit(X_train, y_train)  # scaler fits on train only
pipe.predict(X_test)  # scaler transforms test
```

## 10.3 Feature Engineering Best Practices

```python
# Always transform, never peek
# BAD:
X_test['feature2'] = X_test['feature1'] ** 2  # Uses test info

# GOOD:
# Add in Pipeline
pipe = Pipeline([
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('clf', model)
])

# Handle unknown categories in test
# BAD:
ohe = OneHotEncoder()
ohe.fit_transform(X_train)
X_test_encoded = ohe.transform(X_test)  # May fail on unknown categories

# GOOD:
ohe = OneHotEncoder(handle_unknown='ignore')
ohe.fit_transform(X_train)
X_test_encoded = ohe.transform(X_test)  # Ignores unknown
```

## 10.4 Model Selection Guide

| Task | Algorithm | When to Use |
|------|----------|-------------|
| Classification | RandomForest | Default, interpretable |
| Classification | XGBoost/LightGBM | Best performance |
| Classification | LogisticRegression | Interpretable, linear |
| Regression | Ridge/Lasso | Linear, regularization |
| Regression | RandomForest | Non-linear |
| Regression | GradientBoosting | Best performance |
| Clustering | K-Means | Spherical clusters |
| Clustering | DBSCAN | Arbitrary shapes |
| Dimensionality | PCA | Linear projection |
| Dimensionality | UMAP | Visualization |

## 10.5 Handling Missing Values

```python
# Simple imputation
from sklearn.impute import SimpleImputer, KNNImputer

# Mean imputation
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Median (robust to outliers)
imputer = SimpleImputer(strategy='median')

# Most frequent (categorical)
imputer = SimpleImputer(strategy='most_frequent')

# KNN imputation
imputer = KNNImputer(n_neighbors=5)
X_imputed = imputer.fit_transform(X)

# Add indicator for missing
imputer = SimpleImputer(add_indicator=True, strategy='mean')
```

## 10.6 Hyperparameter Tuning Checklist

```python
# Checklist for hyperparameter search
param_grid = {
    # Linear models
    'classifier__C': [0.01, 0.1, 1, 10],

    # Tree models
    'classifier__max_depth': [3, 5, 10, None],
    'classifier__n_estimators': [50, 100, 200],

    # Regularization
    'classifier__alpha': [0.001, 0.01, 0.1],

    # Class balance
    'classifier__class_weight': [None, 'balanced'],
}

# Use RandomizedSearchCV for large spaces
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_dist = {
    'classifier__max_depth': randint(3, 20),
    'classifier__n_estimators': randint(50, 300),
    'classifier__learning_rate': uniform(0.01, 0.3),
}

search = RandomizedSearchCV(
    pipe, param_dist, n_iter=50, cv=5, random_state=42
)
```

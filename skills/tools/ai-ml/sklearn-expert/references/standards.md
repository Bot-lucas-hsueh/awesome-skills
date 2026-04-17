# Standards & Reference

## 7.1 Official Documentation

- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [User Guide](https://scikit-learn.org/stable/user_guide.html)
- [API Reference](https://scikit-learn.org/stable/modules/classes.html)
- [Examples Gallery](https://scikit-learn.org/stable/auto_examples/index.html)
- [Model Evaluation](https://scikit-learn.org/stable/model_evaluation.html)

## 7.2 Installation

```bash
pip install scikit-learn
pip install scikit-learn[intresh]  # For faster certain algorithms
```

## 7.3 Preprocessing Reference

```python
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler, RobustScaler,
    LabelEncoder, OneHotEncoder,
    PolynomialFeatures, Binarizer
)

# Scaling
scaler = StandardScaler()          # Mean=0, std=1
scaler = MinMaxScaler()            # [0, 1] range
scaler = RobustScaler()            # Median + IQR (outlier-robust)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)

ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
X_cat_encoded = ohe.fit_transform(X_cat)
```

## 7.4 Model Selection Reference

```python
from sklearn.model_selection import (
    train_test_split, cross_val_score,
    GridSearchCV, RandomizedSearchCV,
    StratifiedKFold, KFold
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

# Grid search
param_grid = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
```

## 7.5 Metrics Reference

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_auc_score, roc_curve,
    mean_squared_error, mean_absolute_error, r2_score
)

# Classification
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(classification_report(y_test, y_pred))

# Regression
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

## 7.6 Pipelines Reference

```python
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

# Simple pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier())
])

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

# Column transformer
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['age', 'income']),
    ('cat', OneHotEncoder(), ['gender', 'occupation'])
])

full_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])
```

## 7.7 Ensemble Methods

| Model | Description | Parameters |
|-------|-------------|------------|
| `RandomForestClassifier` | Bagging of decision trees | `n_estimators`, `max_depth` |
| `GradientBoostingClassifier` | Sequential boosting | `n_estimators`, `learning_rate` |
| `AdaBoostClassifier` | Adaptive boosting | `n_estimators`, `learning_rate` |
| `VotingClassifier` | Ensemble of different models | `estimators`, `voting` |
| `StackingClassifier` | Meta-learner on base models | `estimators`, `final_estimator` |

## 7.8 Common Models Quick Reference

```python
from sklearn.linear_model import (
    LinearRegression, LogisticRegression, Ridge, Lasso, ElasticNet
)
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestClassifier, GradientBoostingClassifier,
    AdaBoostClassifier, VotingClassifier
)
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
```

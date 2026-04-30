# python Example

```
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

mlflow.set_experiment("customer-churn")

with mlflow.start_run(run_name="rf_baseline_v1"):
    # Log parameters
    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("random_state", 42)

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    cv_scores = cross_val_score(model, X, y, cv=5)

    # Log metrics
    mlflow.log_metric("train_accuracy", train_acc)
    mlflow.log_metric("test_accuracy", test_acc)
    mlflow.log_metric("cv_mean", cv_scores.mean())
    mlflow.log_metric("cv_std", cv_scores.std())

    # Log model
    mlflow.sklearn.log_model(model, "model", registered_model_name="churn-rf")

    # Log artifacts
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_dict({"description": "RandomForest baseline"}, "config.json")

print(f"Run ID: {mlflow.active_run().info.run_id}")
```

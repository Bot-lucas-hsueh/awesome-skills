# Scenario Examples

## 9.1 A/B Testing Models

**User:** "Compare two model versions in production"

**MLflow Expert:**
> **A/B Testing with Model Registry:**
>
> ```python
> from mlflow.tracking import MlflowClient
>
> client = MlflowClient()
> model_name = "fraud_detection"
>
> # Register candidate model as "Champion"
> candidate_uri = "runs:/candidate_run_id/model"
> client.register_model(candidate_uri, model_name)
>
> # Create evaluation run
> with mlflow.start_run(run_name="ab_test_evaluation"):
>     # Load both models
>     champion = mlflow.pyfunc.load_model(f"models:/{model_name}/Production")
>     challenger = mlflow.pyfunc.load_model(f"models:/{model_name}/Champion")
>
>     # Run A/B test
>     for i, (X, y) in enumerate(test_data):
>         # 80% champion, 20% challenger
>         if hash(X.id) % 100 < 80:
>             pred = champion.predict(X)
>         else:
>             pred = challenger.predict(X)
>
>         log_prediction(i, pred, model_type="champion" if hash(X.id) % 100 < 80 else "challenger")
>
>     # Compare results
>     champion_metrics = evaluate_model("champion")
>     challenger_metrics = evaluate_model("challenger")
>
>     mlflow.log_metrics({
>         "champion_accuracy": champion_metrics["accuracy"],
>         "challenger_accuracy": challenger_metrics["accuracy"],
>     })
>
>     # Promote challenger if better
>     if challenger_metrics["accuracy"] > champion_metrics["accuracy"]:
>         client.transition_model_version_stage(
>             model_name, version=N, stage="Production"
>         )
> ```

## 9.2 Hyperparameter Tuning with Optuna

**User:** "Tune hyperparameters and track with MLflow"

**MLflow Expert:**
> **Optuna + MLflow:**
>
> ```python
> import optuna
> from optuna.samplers import TPESampler
> import mlflow
>
> mlflow.set_experiment("hyperparam_tuning")
>
> def objective(trial):
>     with mlflow.start_run(nested=True):
>         # Sample hyperparameters
>         params = {
>             "n_estimators": trial.suggest_int("n_estimators", 50, 500),
>             "max_depth": trial.suggest_int("max_depth", 3, 20),
>             "min_samples_split": trial.suggest_float("min_samples_split", 0.01, 0.5),
>             "learning_rate": trial.suggest_float("learning_rate", 1e-4, 0.1, log=True),
>         }
>
>         mlflow.log_params(params)
>
>         # Train model
>         model = XGBClassifier(**params)
>         model.fit(X_train, y_train)
>
>         # Evaluate
>         y_pred = model.predict(X_test)
>         accuracy = accuracy_score(y_test, y_pred)
>
>         mlflow.log_metric("accuracy", accuracy)
>
>         return accuracy
>
> # Run optimization
> sampler = TPESampler(seed=42)
> study = optuna.create_study(direction="maximize", sampler=sampler)
> study.optimize(objective, n_trials=100)
>
> print(f"Best accuracy: {study.best_value}")
> print(f"Best params: {study.best_params}")
> ```

## 9.3 Feature Engineering Tracking

**User:** "Track feature engineering steps"

**MLflow Expert:**
> **Feature Engineering Logging:**
>
> ```python
> import mlflow
> from mlflow.models import infer_signature
>
> def engineer_features(df, run_name="feature_engineering"):
>     with mlflow.start_run(run_name=run_name) as run:
>         run_id = run.info.run_id
>
>         # Log original shape
>         mlflow.log_param("original_shape", df.shape)
>
>         # Step 1: Handle missing values
>         df = df.fillna(df.median())
>         mlflow.log_metric("missing_filled", df.isnull().sum().sum())
>
>         # Step 2: Create new features
>         df["total_spend"] = df["quantity"] * df["unit_price"]
>         mlflow.log_param("features_created", ["total_spend"])
>
>         # Step 3: Encode categorical
>         df = pd.get_dummies(df, columns=["category"])
>         mlflow.log_param("final_shape", df.shape)
>
>         # Log feature statistics as artifact
>         stats = df.describe()
>         stats.to_csv("feature_stats.csv")
>         mlflow.log_artifact("feature_stats.csv")
>
>         # Log feature importance (after model training)
>         mlflow.log_dict(feature_importance_dict, "feature_importance.json")
>
>         return df
> ```

## 9.4 Custom Model with PyFunc

**User:** "Log a custom model type"

**MLflow Expert:**
> **Custom PyFunc Model:**
>
> ```python
> import mlflow
> import mlflow.pyfunc
> from sklearn.base import BaseEstimator, TransformerMixin
>
> class FeaturePipeline(BaseEstimator, TransformerMixin):
>     def __init__(self, scaler_type="standard"):
>         self.scaler_type = scaler_type
>
>     def fit(self, X, y=None):
>         from sklearn.preprocessing import StandardScaler, MinMaxScaler
>         if self.scaler_type == "standard":
>             self.scaler = StandardScaler()
>         else:
>             self.scaler = MinMaxScaler()
>         self.scaler.fit(X)
>         return self
>
>     def transform(self, X):
>         return self.scaler.transform(X)
>
> # Wrap in PyFunc
> class FeaturePipelineWrapper(mlflow.pyfunc.PythonModel):
>     def __init__(self, pipeline):
>         self.pipeline = pipeline
>
>     def predict(self, context, model_input):
>         return self.pipeline.transform(model_input)
>
> # Log model
> pipeline = FeaturePipeline(scaler_type="standard")
> pipeline.fit(X_train)
>
> wrapped = FeaturePipelineWrapper(pipeline)
> mlflow.pyfunc.log_model(
>     "feature_pipeline",
>     python_model=wrapped,
>     input_example=X_train[:1]
> )
> ```

## 9.5 Cross-Platform Model Serving

**User:** "Train with MLflow and serve with Triton"

**MLflow Expert:**
> **Export for Triton:**
>
> ```python
> import mlflow
> import torch
>
> # Train model
> model = train_model()
> mlflow.pytorch.log_model(model, "model")
>
> # Export for Triton (requires TensorRT)
> # Load from MLflow
> model_uri = "runs:/run_id/model"
> model = mlflow.pytorch.load_model(model_uri)
>
> # Convert to TorchScript
> scripted = torch.jit.trace(model, example_input)
> scripted.save("model.pt")
>
> # For ONNX export
> mlflow.onnx.log_model(
>     onnx_model,
>     "onnx_model",
>     input_data=input_sample,
>     signature=signature
> )
>
> # Download for deployment
> downloaded_path = mlflow.artifacts.download_artifacts(
>     artifact_uri=f"{model_uri}/model"
> )
> ```

## 9. Scenario Examples

### 9.1 Churn Prediction: SaaS Product

**User:** "Build a churn prediction model for our SaaS product. We have 18 months of user activity data."

**Data Scientist:**
> **SaaS Churn Prediction — End-to-End Implementation**
>
> **Step 1: Problem Framing (before any code)**
>
> Before touching data, clarify:
> - Definition: churn = no login in 30 days? cancelled subscription? downgraded?
> - Label window: predict churn in next 30 days, using features up to T=0 (no future leakage)
> - Business use: trigger retention campaign → need Precision@top-500 users, not overall AUC
> - Baseline: what is current churn rate? (e.g., 8%/month → majority-class baseline = 92% accuracy, useless)
>
> **Step 2: Feature Engineering Pipeline**
> ```python
> import pandas as pd
> import numpy as np
> from sklearn.pipeline import Pipeline
> from sklearn.compose import ColumnTransformer
> from sklearn.preprocessing import StandardScaler, OrdinalEncoder
> from sklearn.impute import SimpleImputer
> from lightgbm import LGBMClassifier
> from sklearn.model_selection import StratifiedKFold, cross_val_score
>
> # Feature engineering: compute as of label date (no leakage past label horizon)
> def build_features(events_df, label_date, lookback_days=90):
>     cutoff = pd.Timestamp(label_date)
>     window = events_df[events_df['event_ts'] < cutoff].copy()
>     window['days_ago'] = (cutoff - window['event_ts']).dt.days
>
>     features = window.groupby('user_id').agg(
>         logins_7d=('event_ts', lambda x: (x >= cutoff - pd.Timedelta('7d')).sum()),
>         logins_30d=('event_ts', lambda x: (x >= cutoff - pd.Timedelta('30d')).sum()),
>         logins_90d=('event_ts', lambda x: x.count()),
>         avg_session_min=('session_duration_min', 'mean'),
>         days_since_last_login=('days_ago', 'min'),
>         feature_adoption_count=('feature_used', 'nunique'),
>         total_payments_90d=('payment_amount', 'sum'),
>     ).reset_index()
>     return features
>
> # Pipeline: prevents train/test leakage in preprocessing
> numerical_cols = ['logins_7d', 'logins_30d', 'logins_90d',
>                   'avg_session_min', 'days_since_last_login',
>                   'feature_adoption_count', 'total_payments_90d']
> categorical_cols = ['subscription_tier', 'acquisition_channel']
>
> preprocessor = ColumnTransformer([
>     ('num', Pipeline([
>         ('impute', SimpleImputer(strategy='median')),
>         ('scale', StandardScaler()),
>     ]), numerical_cols),
>     ('cat', Pipeline([
>         ('impute', SimpleImputer(strategy='most_frequent')),
>         ('encode', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)),
>     ]), categorical_cols),
> ])
>
> model = Pipeline([
>     ('prep', preprocessor),
>     ('clf', LGBMClassifier(
>         n_estimators=500,
>         learning_rate=0.05,
>         num_leaves=63,
>         scale_pos_weight=11,  # ~8% churn rate: (1-0.08)/0.08 ≈ 11
>         random_state=42,
>         n_jobs=-1,
>     )),
> ])
>
> # Stratified CV — preserve class ratio across folds
> cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
> pr_auc_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='average_precision')
> print(f"PR-AUC: {pr_auc_scores.mean():.4f} ± {pr_auc_scores.std():.4f}")
> # Use PR-AUC, not ROC-AUC — churn is imbalanced (8% positive rate)
> ```
>
> **Step 3: Business Impact Translation**
> ```python
> import shap
>
> model.fit(X_train, y_train)
> proba = model.predict_proba(X_test)[:, 1]
>
> # Precision@top-500: how many true churners in top-500 predicted risk?
> top_500_idx = np.argsort(proba)[-500:]
> precision_at_500 = y_test.iloc[top_500_idx].mean()
> print(f"Precision@500: {precision_at_500:.2%}")
> # e.g., 64% → 320 true churners identified in top 500
> # With $500 LTV and 30% save rate: 320 × 0.30 × $500 = $48,000/month recovered
>
> # SHAP for stakeholder explanation
> explainer = shap.TreeExplainer(model['clf'])
> shap_values = explainer.shap_values(model['prep'].transform(X_test))
> shap.summary_plot(shap_values[1], feature_names=numerical_cols + categorical_cols)
> ```
>
> **Key decisions to confirm with you:**
> 1. Is churn defined as "no login in 30 days" or "cancelled subscription"? This changes the label entirely.
> 2. What is the capacity of your retention team? (Determines optimal Precision@K threshold)

---

### 9.2 Model Performance Drop: CTR Declined 15%

**User:** "Our recommendation model's CTR dropped 15% last week. How do we diagnose and fix it?"

**Data Scientist:**
> **Recommendation Model Degradation — Systematic Diagnosis**
>
> A 15% CTR drop has three possible root causes. Diagnose in this order:
>
> **Step 1: Separate Data Issues from Model Issues**
> ```python
> import pandas as pd
> from scipy.stats import ks_2samp
>
> def drift_report(train_df, current_df, feature_cols, psi_threshold=0.2):
>     """PSI > 0.2 = significant drift; 0.1-0.2 = moderate; < 0.1 = stable"""
>     report = []
>     for col in feature_cols:
>         stat, p_val = ks_2samp(
>             train_df[col].dropna(),
>             current_df[col].dropna()
>         )
>         # PSI calculation
>         bins = pd.qcut(train_df[col], q=10, duplicates='drop', retbins=True)[1]
>         train_hist = pd.cut(train_df[col], bins=bins).value_counts(normalize=True) + 1e-8
>         curr_hist  = pd.cut(current_df[col], bins=bins).value_counts(normalize=True) + 1e-8
>         psi = ((curr_hist - train_hist) * np.log(curr_hist
>         report.append({'feature': col, 'ks_stat': stat, 'p_value': p_val, 'psi': psi,
>                        'status': 'DRIFTED' if psi > psi_threshold else 'OK'})
>     return pd.DataFrame(report).sort_values('psi', ascending=False)
>
> drift_df = drift_report(X_train, X_last_week, feature_cols)
> print(drift_df[drift_df['status'] == 'DRIFTED'])
> ```
>
> **Step 2: Root Cause Decision Tree**
>
> | Finding / 发现 | Root Cause / 根因 | Fix
> |---------------|-----------------|-----------|
> | Feature PSI > 0.2 on user activity features | Data drift (behavior changed) | Retrain on last 90 days rolling window |
> | Feature PSI OK but model AUC dropped offline | Concept drift (relationship changed) | Feature refresh + retrain + add recency signal |
> | Feature PSI OK, AUC OK, but CTR dropped | Logging/serving bug — model not the issue | Audit feature pipeline, check serving logs |
> | Specific item category CTR dropped | Catalog change or inventory issue | Filter-level investigation, not model |
>
> **Step 3: Retraining Strategy**
> ```python
> from sklearn.model_selection import TimeSeriesSplit
>
> # Rolling retrain: use last 90 days, weight recent examples higher
> recent_mask = (train_df['event_date'] >= pd.Timestamp('today') - pd.Timedelta('90d'))
> sample_weights = np.where(recent_mask, 3.0, 1.0)  # 3× weight for recent data
>
> model.fit(X_train, y_train, clf__sample_weight=sample_weights)
>
> # Validate with TimeSeriesSplit — never shuffle time-series data
> tscv = TimeSeriesSplit(n_splits=5)
> for fold, (train_idx, val_idx) in enumerate(tscv.split(X)):
>     model.fit(X[train_idx], y[train_idx])
>     val_ndcg = ndcg_score([y[val_idx]], [model.predict_proba(X[val_idx])[:, 1]], k=10)
>     print(f"Fold {fold}: NDCG@10 = {val_ndcg:.4f}")
> ```
>
> **Immediate actions (do these today):**
> 1. Run drift report on all top-20 features
> 2. Check data pipeline logs for upstream failures (missing events, schema changes)
> 3. Compare prediction score distribution between last week and two weeks ago — if distribution shifted, model is seeing different inputs

---

### 9.3 A/B Test Design: New Onboarding Flow / A/B 测试设计：新用户引导流程

**User:** "How do I design an A/B test for our new onboarding flow? We think it will improve 7-day retention."

**Data Scientist:**
> **A/B Test Design — Statistically Rigorous Approach**
>
> **Step 1: Define Metrics Before Building the Test**
>
> - Primary metric: 7-day retention rate (binary: logged in on day 7)
> - Guardrail metrics: D1 retention (should not drop), time-to-first-value (should not increase)
> - Minimum Detectable Effect (MDE): what lift justifies the engineering investment? (e.g., +2pp retention)
>
> **Step 2: Power Analysis — Calculate Required Sample Size**
> ```python
> from statsmodels.stats.proportion import proportion_effectsize, proportions_ztest
> from statsmodels.stats.power import TTestIndPower
> import numpy as np
>
> # Parameters — define BEFORE looking at experiment data
> baseline_retention = 0.35   # current 7-day retention: 35%
> mde_absolute       = 0.02   # minimum detectable effect: +2 percentage points
> alpha              = 0.05   # Type I error (false positive rate)
> power              = 0.80   # 1 - Type II error (false negative rate)
>
> # Cohen's h effect size for proportions
> effect_size = proportion_effectsize(baseline_retention + mde_absolute, baseline_retention)
>
> analysis = TTestIndPower()
> n_per_group = analysis.solve_power(
>     effect_size=effect_size,
>     alpha=alpha,
>     power=power,
>     ratio=1.0,
>     alternative='two-sided',
> )
> n_per_group = int(np.ceil(n_per_group))
>
> print(f"Effect size (Cohen's h): {effect_size:.4f}")
> print(f"Required per group: {n_per_group:,}")
> print(f"Total sample size:  {n_per_group * 2:,}")
>
> # How many days to run at current signup rate?
> daily_signups = 3000  # new users per day
> test_days = np.ceil((n_per_group * 2)
> print(f"Test duration: {int(test_days)} days at {daily_signups:,} signups/day")
> ```
>
> **Step 3: Analysis — Avoid the Peeking Problem**
> ```python
> from scipy.stats import chi2_contingency
> import pandas as pd
>
> # Analyze ONLY after reaching pre-specified sample size
> results = pd.DataFrame({
>     'group':    ['control', 'treatment'],
>     'retained': [1085, 1148],
>     'total':    [3100, 3100],
> })
> results['churned'] = results['total'] - results['retained']
> results['retention_rate'] = results['retained']
>
> contingency = results[['retained', 'churned']].values
> chi2, p_value, dof, expected = chi2_contingency(contingency)
>
> control_rate   = results.loc[0, 'retention_rate']
> treatment_rate = results.loc[1, 'retention_rate']
> lift_pp        = treatment_rate - control_rate
> lift_relative  = lift_pp
>
> print(f"Control:   {control_rate:.1%}")
> print(f"Treatment: {treatment_rate:.1%}")
> print(f"Absolute lift: {lift_pp:+.2%} ({lift_relative:+.1%} relative)")
> print(f"p-value: {p_value:.4f} — {'SIGNIFICANT' if p_value < alpha else 'NOT SIGNIFICANT'}")
> ```
>
> **Critical pitfalls in this specific experiment:**
> - Day-of-week effect: onboarding experience differs on weekday vs. weekend; run for full weeks
> - Novelty effect: new onboarding may spike D1 but not D7; wait the full retention window
> - Carryover: if you run multiple onboarding tests simultaneously, use holdout groups
> - SRM check: verify control and treatment group sizes match the intended split (50/50 ± 2%)

---

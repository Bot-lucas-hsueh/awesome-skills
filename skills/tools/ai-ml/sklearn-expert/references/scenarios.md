# Scenario Examples

## 9.1 Imbalanced Classification

**User:** "Handle imbalanced dataset for fraud detection"

**Sklearn Expert:**
> **Imbalanced Data Pipeline:**
>
> ```python
> from sklearn.utils import resample
> from imblearn.over_sampling import SMOTE
> from imblearn.pipeline import Pipeline as ImbPipeline
>
> # Option 1: Class weights
> clf = RandomForestClassifier(
>     class_weight='balanced',  # Auto-balance
>     random_state=42
> )
>
> # Option 2: SMOTE oversampling
> smote = SMOTE(random_state=42)
> X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
>
> # Option 3: Undersampling majority
> from imblearn.under_sampling import RandomUnderSampler
> rus = RandomUnderSampler(random_state=42)
> X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
>
> # Option 4: Combined SMOTE + undersampling
> from imblearn.combine import SMOTETomek
> smote_tomek = SMOTETomek(random_state=42)
> X_resampled, y_resampled = smote_tomek.fit_resample(X_train, y_train)
> ```

## 9.2 Clustering Analysis

**User:** "Find natural clusters in customer data"

**Sklearn Expert:**
> **Clustering Pipeline:**
>
> ```python
> from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
> from sklearn.metrics import silhouette_score
> from sklearn.preprocessing import StandardScaler
>
> # Prepare data
> scaler = StandardScaler()
> X_scaled = scaler.fit_transform(X)
>
> # K-Means with elbow method
> inertias = []
> silhouettes = []
> K_range = range(2, 11)
>
> for k in K_range:
>     kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
>     labels = kmeans.fit_predict(X_scaled)
>     inertias.append(kmeans.inertia_)
>     silhouettes.append(silhouette_score(X_scaled, labels))
>
> # Best k from silhouette
> best_k = K_range[np.argmax(silhouettes)]
>
> # Final clustering
> final_kmeans = KMeans(n_clusters=best_k, n_init=10, random_state=42)
> cluster_labels = final_kmeans.fit_predict(X_scaled)
>
> # Add clusters to dataframe
> df['cluster'] = cluster_labels
> ```

## 9.3 Dimensionality Reduction

**User:** "Reduce features for visualization"

**Sklearn Expert:**
> **Dimensionality Reduction:**
>
> ```python
> from sklearn.decomposition import PCA, TruncatedSVD
> from sklearn.manifold import TSNE, UMAP
>
> # PCA
> pca = PCA(n_components=2)
> X_pca = pca.fit_transform(X_scaled)
>
> print(f"Explained variance: {pca.explained_variance_ratio_}")
> print(f"Total: {sum(pca.explained_variance_ratio_):.2%}")
>
> # t-SNE (good for visualization)
> tsne = TSNE(n_components=2, random_state=42, perplexity=30)
> X_tsne = tsne.fit_transform(X_scaled)
>
> # UMAP (faster and better preservation)
> import umap
> reducer = umap.UMAP(n_components=2, random_state=42)
> X_umap = reducer.fit_transform(X_scaled)
> ```

## 9.4 Anomaly Detection

**User:** "Detect outliers in data"

**Sklearn Expert:**
> **Anomaly Detection:**
>
> ```python
> from sklearn.ensemble import IsolationForest
> from sklearn.neighbors import LocalOutlierFactor
>
> # Isolation Forest
> iso_forest = IsolationForest(
>     contamination=0.1,  # Expected proportion of outliers
>     random_state=42
> )
> outlier_labels = iso_forest.fit_predict(X)
>
> # Get outlier scores
> outlier_scores = iso_forest.score_samples(X)
>
> # LOF (Local Outlier Factor)
> lof = LocalOutlierFactor(
>     n_neighbors=20,
>     contamination=0.1
> )
> outlier_labels = lof.fit_predict(X)
>
> # Remove outliers
> X_clean = X[outlier_labels == 1]
> y_clean = y[outlier_labels == 1]
> ```

## 9.5 Multi-Label Classification

**User:** "Handle multi-label output"

**Sklearn Expert:**
> **Multi-Label Pipeline:**
>
> ```python
> from sklearn.multioutput import MultiOutputClassifier
> from sklearn.multiclass import OneVsRestClassifier
>
> # Multi-output classifier
> clf = MultiOutputClassifier(
>     RandomForestClassifier(random_state=42)
> )
> clf.fit(X_train, y_train_multilabel)
> y_pred = clf.predict(X_test)
>
> # OneVsRest for binary multi-label
> clf = OneVsRestClassifier(
>     LogisticRegression()
> )
> clf.fit(X_train, y_train_multilabel)
> y_pred = clf.predict(X_test)
>
> # Get probability estimates
> y_prob = clf.predict_proba(X_test)
> ```

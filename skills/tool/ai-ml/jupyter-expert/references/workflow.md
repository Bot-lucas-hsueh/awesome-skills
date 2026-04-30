# Standard Workflow

## 8.1 Data Exploration Workflow

```
Phase 1: Environment Setup
├── Install required packages
├── Set up ipykernel
└── Verify kernel is active

Phase 2: Data Loading
├── Load data with pandas
├── Use %time to measure load time
└── Check memory usage with %memit

Phase 3: Initial Exploration
├── Display head/tail with display()
├── Use df.info() and df.describe()
├── Check dtypes and missing values
└── Use %who to see variables

Phase 4: Visualization
├── Inline matplotlib: %matplotlib inline
├── Interactive plots: %matplotlib widget
└── Use seaborn for statistical plots

Phase 5: Analysis & Export
├── Document findings in markdown cells
├── Export results to CSV/JSON
└── Convert notebook to report
```

## 8.2 ML Experiment Workflow

```python
# Cell 1: Imports and setup
%matplotlib inline
%load_ext autoreload
%autoreload 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Cell 2: Load data
df = pd.read_csv('data.csv')
print(f"Shape: {df.shape}")
display(df.head())

# Cell 3: Preprocessing
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Cell 4: Training with timing
%time model.fit(X_train_scaled, y_train)

# Cell 5: Evaluation
from sklearn.metrics import classification_report, confusion_matrix

y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

# Cell 6: Save model
import joblib
joblib.dump(model, 'model.pkl')
```

## 8.3 Debugging Workflow

```python
# Enable automatic debugging on errors
%pdb on

# Post-mortem debugging after error
%debug

# Interactive debugger in cell
%%writefile debug_test.py
def problematic_function():
    import pdb; pdb.set_trace()
    # ... code ...
    
# Profile specific function
%prun model.fit(X_train, y_train)

# Memory profiling
%memit model.fit(X_train, y_train)
```

## 8.4 Interactive Widget Workflow

```python
import ipywidgets as widgets
from IPython.display import display

# Create interactive widget
@widgets.interact
def plot_data(column=['col1', 'col2', 'col3'], 
              bins=(10, 100, 10)):
    plt.hist(df[column], bins=bins)
    plt.show()

# Slider widget
slider = widgets.IntSlider(
    value=50,
    min=0,
    max=100,
    step=5,
    description='Threshold:'
)
display(slider)

# Button widget
button = widgets.Button(description="Run Model")
output = widgets.Output()

def on_click(b):
    with output:
        print("Running...")
        
button.on_click(on_click)
display(button, output)
```

## 8.5 Notebook Conversion Workflow

```python
# In terminal, convert notebook to various formats

# 1. Execute notebook with output cleared
jupyter nbconvert --to notebook --execute --inplace mynotebook.ipynb

# 2. Convert to HTML with table of contents
jupyter nbconvert --to html_tocf mynotebook.ipynb

# 3. Convert to PDF via LaTeX
jupyter nbconvert --to pdf mynotebook.ipynb

# 4. Create presentation slides
jupyter nbconvert --to slides mynotebook.ipynb --reveal-prefix reveal.js

# 5. Extract to Python script
jupyter nbconvert --to script mynotebook.ipynb

# 6. Clean output before committing
jupyter nbconvert --to notebook --clear-output mynotebook.ipynb
```

## 8.6 Remote Jupyter Workflow

```bash
# SSH into remote server and start Jupyter
ssh user@remote-server
jupyter lab --port=8888 --no-browser --ip=0.0.0.0

# From local machine, create SSH tunnel
ssh -L 8888:localhost:8888 user@remote-server

# Or use VS Code Remote SSH extension
# It handles tunneling automatically

# Alternative: use JupyterHub for multi-user setup
# jupyterhub --ip=0.0.0.0 --port=8888
```

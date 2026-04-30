# Scenario Examples

## 9.1 Data Exploration with Profiling

**User:** "Explore a large dataset efficiently"

**Jupyter Expert:**
> **Data Exploration Pipeline:**
>
> ```python
> # Load and profile dataset
> import pandas as pd
> import ydata_profiling as pp
>
> df = pd.read_csv('large_dataset.csv')
>
> # Generate profile report
> profile = pp.ProfileReport(df, 
>                            title="Dataset Profile",
>                            explorative=True)
>
> # Display inline
> profile.to_widgets()
>
> # Or save to file
> profile.to_file("report.html")
>
> # Quick stats without full profile
> display(df.describe())
> print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
> ```

## 9.2 Parallel Processing in Notebook

**User:** "Speed up data processing with parallel execution"

**Jupyter Expert:**
> **Parallel Processing:**
>
> ```python
> from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
> import multiprocessing
>
> # Get CPU count
> n_cores = multiprocessing.cpu_count()
> print(f"Available cores: {n_cores}")
>
> # Define worker function
> def process_chunk(chunk_data):
>     # Process each chunk
>     return chunk_data.apply(some_function)
>
> # Split data into chunks
> chunks = np.array_split(df, n_cores * 4)
>
> # Parallel execution
> with ProcessPoolExecutor(max_workers=n_cores) as executor:
>     results = list(executor.map(process_chunk, chunks))
>
> # Combine results
> result_df = pd.concat(results)
> ```

## 9.3 Custom Magic Command

**User:** "Create a reusable magic command for my workflow"

**Jupyter Expert:**
> **Custom Magic:**
>
> ```python
> from IPython.core.magic import register_line_magic, register_cell_magic
>
> @register_line_magic
> def loadcsv(line):
>     """Load CSV and display shape"""
>     import pandas as pd
>     df = pd.read_csv(line)
>     print(f"Loaded {df.shape}")
>     return df
>
> @register_cell_magic
> def timer(line, cell):
>     """Time cell execution"""
>     import time
>     start = time.time()
>     get_ipython().ex(cell)
>     print(f"Execution time: {time.time() - start:.2f}s")
>
> # Use magic
> # %loadcsv data.csv
> # %%timer
> # code here...
> ```

## 9.4 Creating Interactive Dashboards

**User:** "Build an interactive data dashboard in Jupyter"

**Jupyter Expert:**
> **Dashboard with Widgets:**
>
> ```python
> import ipywidgets as widgets
> from IPython.display import display, clear_output
> import matplotlib.pyplot as plt
>
> # Create dropdowns
> x_col = widgets.Dropdown(options=df.columns, description='X:')
> y_col = widgets.Dropdown(options=df.columns, description='Y:')
> color_col = widgets.Dropdown(options=['None'] + list(df.columns), 
>                              description='Color:')
> plot_type = widgets.Dropdown(options=['scatter', 'line', 'hist'], 
>                               description='Plot:')
>
> # Output area
> output = widgets.Output()
>
> def update_plot(change):
>     with output:
>         clear_output(wait=True)
>         plt.figure(figsize=(10, 6))
>         if plot_type.value == 'scatter':
>             plt.scatter(df[x_col.value], df[y_col.value], 
>                        c=df[color_col.value] if color_col.value != 'None' else None)
>         plt.xlabel(x_col.value)
>         plt.ylabel(y_col.value)
>         plt.title(f'{plot_type.value.title()} Plot')
>         plt.show()
>
> # Connect callbacks
> for widget in [x_col, y_col, color_col, plot_type]:
>     widget.observe(update_plot, names='value')
>
> # Display dashboard
> display(widgets.VBox([x_col, y_col, color_col, plot_type, output]))
> ```

## 9.5 Git Integration in JupyterLab

**User:** "Version control my notebook changes"

**Jupyter Expert:**
> **Git Workflow:**
>
> ```python
> # Use jupyterlab-git extension
> # Or use nbstripout for notebook cleaning
>
> # Install nbstripout
> !pip install nbstripout
>
> # Configure for your repo
> !git nbstripout --install --global
>
> # Commit changes
> !git add notebook.ipynb
> !git commit -m "Update model parameters"
>
> # View diff (before committing)
> !git diff notebook.ipynb
>
> # Use nbdime for better diff visualization
> !pip install nbdime
> !nbdiff-web  # Opens diff viewer
> ```

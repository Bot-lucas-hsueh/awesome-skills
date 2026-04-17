# Standards & Reference

## 7.1 Official Documentation

- [Jupyter Documentation](https://docs.jupyter.org/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [IPython Reference](https://ipython.readthedocs.io/)
- [Jupyter Notebook Docs](https://jupyter-notebook.readthedocs.io/)
- [nbconvert Docs](https://nbconvert.readthedocs.io/)
- [Jupyter Widgets](https://ipywidgets.readthedocs.io/)

## 7.2 Installation

```bash
# Core packages
pip install jupyterlab
pip install notebook
pip install ipykernel
pip install ipywidgets

# Kernel installation
python -m ipykernel install --user --name myenv --display-name "My Environment"

# Nbconvert for notebook conversion
pip install nbconvert
pip install nbformat
```

## 7.3 Magic Commands Reference

### Timing Magic

| Magic | Description | Example |
|-------|-------------|---------|
| `%time` | Time single statement | `%time [x**2 for x in range(1000)]` |
| `%%time` | Time entire cell | `%%time\nfor i in range(1000):\n    pass` |
| `%timeit` | Time with iterations | `%timeit -n 100 x.sort()` |
| `%%timeit` | Time cell with iterations | `%%timeit -n 100 -r 10` |

### Execution Magic

| Magic | Description |
|-------|-------------|
| `%run` | Execute Python file in notebook |
| `%load` | Load code into cell from file/URL |
| `%paste` | Paste clipboard code |
| `%cpaste` | Interactive paste mode |
| `%who` | List all interactive variables |
| `%whos` | List variables with details |
| `%xdel` | Delete variable from namespace |

### Debugging Magic

| Magic | Description |
|-------|-------------|
| `%debug` | Activate post-mortem debugger |
| `%pdb` | Toggle automatic debugging |
| `%prun` | Profile with cProfile |
| `%lprun` | Line-by-line profiling |
| `%memit` | Memory measurement |
| `%mprun` | Memory profiling |

### System Magic

| Magic | Description |
|-------|-------------|
| `%cd` | Change directory |
| `%pwd` | Print working directory |
| `%ls` | List directory contents |
| `%env` | Environment variables |
| `%set_env` | Set environment variable |
| `%pip` | Run pip commands |
| `%conda` | Run conda commands |

## 7.4 JupyterLab Extensions

```bash
# Install extension manager
pip install jupyterlab-lsp
pip install jupyterlab-git
pip install @jupyter-widgets/jupyterlab-manager

# Enable extensions
jupyter labextension enable @jupyterlab/git
jupyter server extension enable jupyterlab_git
```

## 7.5 Configuration Files

```python
# jupyter_lab_config.py location
# ~/.jupyter/jupyter_lab_config.py

c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.token = ''  # Disable token (not recommended for prod)

# Kernel configuration
c.KernelManager.auto_start_kernel = True
c.MappingKernelManager.default_kernel_name = 'python3'
```

## 7.6 Remote Server Setup

```bash
# On remote server
jupyter lab --port=8888 --no-browser --ip=0.0.0.0

# SSH tunnel from local machine
ssh -L 8888:localhost:8888 user@remote-server

# Then open browser to http://localhost:8888
```

## 7.7 Notebook Conversion Commands

```bash
# Convert to different formats
jupyter nbconvert --to notebook --execute input.ipynb --output output.ipynb
jupyter nbconvert --to python input.ipynb --output script.py
jupyter nbconvert --to html input.ipynb
jupyter nbconvert --to pdf input.ipynb
jupyter nbconvert --to markdown input.ipynb
jupyter nbconvert --to slides input.ipynb

# With execution timeout
jupyter nbconvert --to python --execute --ExecutePreprocessor.timeout=600 input.ipynb
```

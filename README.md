## Setup Guide (Windows + VS Code)

### 1. Install UV

Open the VS Code terminal and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart the terminal and verify:

```powershell
uv --version
```


### 2. Clone the Repository

```powershell
git clone https://github.com/MDSalman22415/Session-Project.git
cd Session-Project
```

### 3. Install Python 3.12

```powershell
uv python install 3.12
```

### 4. Create the Virtual Environment

```powershell
uv venv --python 3.12
```

### 5. Install Project Dependencies

If `pyproject.toml` and `uv.lock` are available:

```powershell
uv sync
```

If using `requirements.txt` instead:

```powershell
uv pip install --python ".venv\Scripts\python.exe" -r requirements.txt
```

### 6. Install Jupyter Notebook and IPython Kernel

Run these commands inside the project environment:

```powershell
uv add jupyter ipykernel
```

If the project uses `requirements.txt` instead of `pyproject.toml`, run:

```powershell
uv pip install --python ".venv\Scripts\python.exe" jupyter ipykernel
```

### 7. Register the Python Kernel

```powershell
uv run python -m ipykernel install --user --name mi-hub --display-name "Python (MI HUB)"
```

### 8. Install VS Code Extensions

Run the following commands if the VS Code CLI is available:

```powershell
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

### 9. Open the Project

```powershell
code .
```

Open `Titanic_End_to_End_ML_DL.ipynb`.

### 10. Select the Jupyter Kernel

1. Click **Select Kernel** in the notebook's top-right corner.
2. Select **Python (MI HUB)** or the project's `.venv` Python interpreter.
3. If prompted, trust the notebook only if you trust its source.
4. Run the notebook cells from top to bottom.

### 11. Verify the Kernel

Run this cell in the notebook:

```python
import sys
print(sys.executable)
```

The path should point to the project's `.venv` environment.

### 12. Dataset and Model Files

Check that the required dataset files (`train.csv`, `test.csv`, and any other required files) are present in the repository before running the notebook. If a required file is missing, obtain it and place it in the location expected by the notebook.

**Important:** Use the project's dependency versions to avoid compatibility warnings when loading saved models. Do not load model files from untrusted sources.

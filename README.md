git add README.md# ML Project Setup (Windows + VS Code)

### Step 1: Install UV

Open the VS Code terminal (\`Ctrl + \`\`) and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart the terminal and verify:

```powershell
uv --version
```

### Step 2: Download the Project

```powershell
git clone https://github.com/MDSalman22415/Session-Project.git
cd YOUR_PROJECT_FOLDER
```

### Step 3: Install Python

```powershell
uv python install 3.12
```

### Step 4: Create the Virtual Environment

```powershell
uv venv --python 3.12
```

### Step 5: Install Project Libraries

If the project contains `requirements.txt`:

```powershell
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
```

If the project contains `pyproject.toml` and `uv.lock`:

```powershell
uv sync
```

Use the command matching the files in your repository.

### Step 6: Open the Project

```powershell
code .
```

In VS Code, install the **Python** and **Jupyter** extensions from the Extensions panel if they are not already installed.

### Step 7: Select the Notebook Kernel

1. Open the `.ipynb` notebook.
2. Click **Select Kernel**.
3. Choose the Python interpreter inside `.venv`.
4. Run the notebook cells from top to bottom.

### Step 8: Dataset

Download the required dataset if it is not included in the repository, and place it in the folder expected by the notebook.

**Important:** Keep `requirements.txt` or `pyproject.toml` updated with all libraries used by the project, including TensorFlow if the ANN notebook requires it. Users should not need to install each library separately.

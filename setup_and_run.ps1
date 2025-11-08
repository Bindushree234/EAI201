# Navigate to project folder
cd "$PSScriptRoot"

# Delete old venv if exists
if (Test-Path .\venv) { Remove-Item -Recurse -Force .\venv }

# Create new virtual environment
python -m venv venv

# Activate venv
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install streamlit pandas openpyxl scikit-learn matplotlib

# Create app.py if not exists
if (-Not (Test-Path .\app.py)) {
    New-Item -Name "app.py" -ItemType "file"
    Write-Host "Created empty app.py. Paste the Streamlit code."
}

# Run Streamlit
streamlit run app.py

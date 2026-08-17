where /q python || winget install --id=Python.Python --source=winget --interactive
where /q gpg || winget install --id=GnuPG.Gpg4win --source=winget --interactive

python -m venv ./venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py

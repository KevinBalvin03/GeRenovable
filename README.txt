Si es primera vez ejecutar todos los siguientes comandos en la terminal y si es segunda vez omitir los 4 primeros 
python3 -m venv venv
python.exe -m pip install --upgrade pip
pip install "fastapi[all]"
pip install python-multipart



venv\Scripts\Activate.ps1  //si es powershell venv\Scripts\activate.bat
uvicorn main:app --reload

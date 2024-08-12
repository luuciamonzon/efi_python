
#Clonar el proyecto:\
    git clone https://https://github.com/luuciamonzon/efi_python.git
    cd efi_python\
#Crear el entorno virtual:\
    python3 -m venv .env\
#Activar el entorno virtual:\
    source .env/bin/activate\
#Instalar requerimientos:\
    pip install -r requirements.txt\
#Configura la base de datos en app.py / revisar que la URL de la base de datos coincida:\
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/efi_python"\
#Inicializar la base de datos:\
    flask db init\ 
    flask db migrate -m "creacion de la migracion"\
    flask db upgrade\
#Correr el proyecto:\
    flask run --reload\

from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask (__name__)

#Configuración de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/efi_python"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



from models import Marca, Equipo, Proveedor, Reclamo

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/marcas", methods=["POST","GET"])
def marcas():
    
    marcas= Marca.query.all()

    if request.method=="POST":
        nombre = request.form["nombre"]
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for("marcas"))

    return render_template("marcas.html", marcas=marcas)

@app.route("/marca/<id>/equipos")
def equipos_por_marca(id):
    marca = Marca.query.get_or_404(id)
    equipos = marca.equipos
    return render_template(
        "equipos_by_marca.html", 
        equipos = equipos,
        marca = marca
        )


@app.route("/marca/<int:id>/editar", methods=['GET', 'POST'])
def marca_editar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template(
        "marca_edit.html",
        marca=marca
    )

@app.route("/marca/<int:id>/eliminar", methods=['GET', 'POST'])
def marca_eliminar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(marca)
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template("marca_eliminar.html", marca=marca)


@app.route("/equipos", methods=["POST", "GET"])
def equipos():
    equipos = Equipo.query.all()
    marcas = Marca.query.all()

    if request.method == "POST":
        nombre = request.form["nombre"]
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        precio = request.form["precio"]
        anio = request.form["anio_de_fabricacion"]
        caracteristicas = request.form["caracteristicas"]
        equipo_nuevo = Equipo(
            nombre=nombre, 
            marca_id=marca,
            modelo=modelo,
            precio=precio,
            anio_de_fabricacion=anio,
            caracteristicas=caracteristicas
        )
        db.session.add(equipo_nuevo)
        db.session.commit()
        return redirect(url_for("equipos"))

    return render_template(
        "equipos.html", 
        equipos=equipos,
        marcas=marcas,
    )

@app.route("/equipos/<int:id>/editar", methods=['GET', 'POST'])
def equipo_editar(id):
    equipo = Equipo.query.get_or_404(id)
    marcas = Marca.query.all()  # Necesario para el formulario de edición

    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.marca_id = request.form['marca']
        equipo.modelo = request.form['modelo']
        equipo.precio = request.form['precio']
        equipo.anio_de_fabricacion = request.form['anio_de_fabricacion']
        equipo.caracteristicas = request.form['caracteristicas']
        db.session.commit()
        return redirect(url_for('equipos'))

    return render_template(
        "equipos_edit.html",
        equipo=equipo,
        marcas=marcas
    )

@app.route("/equipos/<int:id>/eliminar", methods=['GET', 'POST'])
def equipo_eliminar(id):
    equipo = Equipo.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(equipo)
        db.session.commit()
        return redirect(url_for('equipos'))

    return render_template("equipos_eliminar.html", equipo=equipo)


@app.route("/proveedores", methods=["POST", "GET"])
def proveedores():
    proveedores = Proveedor.query.all()

    if request.method == "POST":
        nombre = request.form.get("nombre")
        nro_telefono = request.form.get("nro_telefono")
        direccion = request.form.get("direccion")
        cuit = request.form.get("cuit")
        
        # Verifica que todos los campos necesarios estén presentes
        if nombre and nro_telefono and direccion and cuit:
            nuevo_proveedor = Proveedor(
                nombre=nombre,
                nro_telefono=nro_telefono,
                direccion=direccion,
                cuit=cuit
            )
            db.session.add(nuevo_proveedor)
            db.session.commit()
            return redirect(url_for("proveedores"))

    return render_template("proveedores.html", proveedores=proveedores)



@app.route("/proveedor/<int:id>/editar", methods=['GET', 'POST'])
def proveedor_editar(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.nro_telefono = request.form['nro_telefono']
        proveedor.direccion = request.form['direccion']
        proveedor.cuit = request.form['cuit']
        db.session.commit()
        return redirect(url_for('proveedores'))

    return render_template("proveedor_edit.html", proveedor=proveedor)


@app.route("/proveedores/<int:id>/eliminar", methods=['GET', 'POST'])
def proveedor_eliminar(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(proveedor)
        db.session.commit()
        return redirect(url_for('proveedores'))  #redirige a la lista de proveedores

    return render_template("proveedores_eliminar.html", proveedor=proveedor)


@app.route("/reclamos", methods=["POST", "GET"])
def reclamos():
    reclamos = Reclamo.query.all()

    if request.method == "POST":
        nombre = request.form["nombre"]
        nro_telefono = request.form["nro_telefono"]
        direccion = request.form["direccion"]
        detalle = request.form["detalle"]
        nuevo_reclamo = Reclamo(
            nombre=nombre,
            nro_telefono=nro_telefono,
            direccion=direccion,
            reclamo=detalle
        )
        db.session.add(nuevo_reclamo)
        db.session.commit()
        return redirect(url_for("reclamos"))

    return render_template("reclamos.html", reclamos=reclamos)

@app.route("/reclamos/<int:id>/editar", methods=['GET', 'POST'])
def reclamo_editar(id):
    reclamo = Reclamo.query.get_or_404(id)

    if request.method == 'POST':
        reclamo.nombre = request.form['nombre']
        reclamo.nro_telefono = request.form['nro_telefono']
        reclamo.direccion = request.form['direccion']
        reclamo.reclamo = request.form['detalle']
        db.session.commit()
        return redirect(url_for('reclamos'))

    return render_template("reclamos_edit.html", reclamo=reclamo)

@app.route("/reclamos/<int:id>/eliminar", methods=['GET', 'POST'])
def reclamo_eliminar(id):
    reclamo = Reclamo.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(reclamo)
        db.session.commit()
        return redirect(url_for('reclamos'))

    return render_template("reclamos_eliminar.html", reclamo=reclamo)



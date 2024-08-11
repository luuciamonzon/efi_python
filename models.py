from app import db

class Marca (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer)
    anio_de_fabricacion = db.Column(db.Integer)
    caracteristicas = db.Column(db.String(4000))

    # Pertenece a:
    marca_id = db.Column(db.Integer, db.ForeignKey("marca.id"), nullable=False)

    # Relación directa con el otro objeto:
    marca = db.relationship("Marca", backref=db.backref("equipos", lazy=True))
    

class Proveedor (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    nro_telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(50))
    cuit = db.Column(db.String(20), nullable=False)


class Reclamo (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    nro_telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    reclamo = db.Column(db.String(1000), nullable=False)








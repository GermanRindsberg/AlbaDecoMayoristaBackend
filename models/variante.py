from config.db import db, BaseModelMixin
from models.producto import Producto

class Variante(db.Model, BaseModelMixin):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    color= db.Column(db.String(100), unique=False)
    activo=db.Column(db.Integer)
    #FORANEAS
    idProducto = db.Column(db.Integer, db.ForeignKey(Producto.id), unique=False)
    producto = db.relationship("Producto", uselist=False)

       
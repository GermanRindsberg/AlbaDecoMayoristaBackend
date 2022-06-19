from config.db import db, BaseModelMixin
from models.foto import Foto
from models.subCategoria import SubCategoria
from models.categoria import Categoria

class Producto(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre= db.Column(db.String(100))
    alto= db.Column(db.Integer)
    ancho= db.Column(db.Integer)
    largo= db.Column(db.Integer)
    precio= db.Column(db.Float)
    capacidad= db.Column(db.Float)
    descripcion= db.Column(db.String(800))
    activo=db.Column(db.String(10))

    #FORANEAS
    #la idSubCategoria apunta a una entidad padre, en este caso subCategoria, el campo subCategoria pertenece al padre
    idSubCategoria=db.Column(db.Integer, db.ForeignKey(SubCategoria.id), unique=False)
    subCategoria=db.relationship("SubCategoria", uselist=False)
    idCategoria=db.Column(db.Integer, db.ForeignKey(Categoria.id), unique=False)
    categoria=db.relationship("Categoria", uselist=False)
    #variantes
    #variantes y fotos trae todas las hijas que apunten a este idProducto
    variantes= db.relationship('Variante', lazy='select', back_populates='producto')
    #fotos
    fotos = db.relationship(Foto, lazy='select', back_populates='producto')
        
    

    



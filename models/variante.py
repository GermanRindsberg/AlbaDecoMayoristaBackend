from config.db import db, BaseModelMixin
from models.producto import Producto

class Variante(db.Model, BaseModelMixin):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    color= db.Column(db.String(100), unique=False)
    #FORANEAS
    idProducto = db.Column(db.Integer, db.ForeignKey(Producto.id), unique=False)
    producto = db.relationship("Producto", uselist=False)
    
    @classmethod
    def eliminarVariantePorIdProducto(self, idProducto):
        producto=Producto.get_by_id(idProducto)
        for variantes in producto.variantes:
            Variante.delete(variantes)
        return True
         
       
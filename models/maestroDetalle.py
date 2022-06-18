from models.producto import Producto
from models.variante import Variante
from config.db import db, BaseModelMixin


class MaestroDetalle(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    idPedido=db.Column(db.Integer, db.ForeignKey("pedido.id"), unique=False)
    idProducto = db.Column(db.Integer, db.ForeignKey(Producto.id), unique=False)
    idVariante = db.Column(db.Integer, db.ForeignKey(Variante.id), unique=False)
    precioUnitario = db.Column(db.Float)
    cantidad = db.Column(db.Integer)
    subTotal = db.Column(db.Float)

    pedido = db.relationship("Pedido", uselist=False)
    variante = db.relationship(Variante, uselist=False)
    producto = db.relationship(Producto, uselist=False)
    

  
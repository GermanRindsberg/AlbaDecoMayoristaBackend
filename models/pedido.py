from config.db import db, BaseModelMixin
from models.maestroDetalle import MaestroDetalle


class Pedido(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fechaPedido= db.Column(db.Date())
    subTotal=db.Column(db.Float)
    descuento=db.Column(db.Float)
    montoTotal=db.Column(db.Float)
    fechaSeña= db.Column(db.Date())
    estado=db.Column(db.String(100))
    fechaEnvio= db.Column(db.Date())
    numeroGuia=db.Column(db.String(200))
    transporte=db.Column(db.String(200))
    #FORANEAS
    maestroDetalle=db.relationship(MaestroDetalle, lazy='select', back_populates='pedido') 
    usuario=db.relationship("Usuario", lazy='select') 
    idUsuario=db.Column(db.Integer, db.ForeignKey("usuario.id"), unique=False)

    @classmethod
    def getPorIdUsuario(cls, idUsuario):
        listadoProductos = cls.query.filter_by(idUsuario=idUsuario).all()
        return listadoProductos
        
  

 
    

    



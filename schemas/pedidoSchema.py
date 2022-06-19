from config.marsh import ma
from models.pedido import Pedido
from schemas.maestroDetalleSchema import maestroDetallesSchema

class PedidoSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Pedido
    id = ma.auto_field()
    subTotal = ma.auto_field()
    descuento = ma.auto_field()
    montoTotal=ma.auto_field()
    fechaPedido= ma.auto_field()
    fechaSeña= ma.auto_field()
    fechaEnvio=ma.auto_field()
    numeroGuia=ma.auto_field()
    transporte=ma.auto_field()
    estado = ma.auto_field()
    idUsuario=ma.auto_field()
    #FORANEAS
    maestroDetalle=ma.Nested(maestroDetallesSchema)
    
    
pedidoSchema = PedidoSchema()
pedidosSchema = PedidoSchema(many=True)

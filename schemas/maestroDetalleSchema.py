from schemas.productoSchema import ProductoSchemaParaMaestroDetalle
from schemas.varianteSchema import VarianteSchema

from config.marsh import ma
from models.maestroDetalle import MaestroDetalle


class MaestroDetalleSchema(ma.SQLAlchemySchema):
    class Meta:
        model=MaestroDetalle
    #id =ma.auto_field()
    idPedido=ma.auto_field()
    precioUnitario=ma.auto_field()
    cantidad=ma.auto_field()
    subTotal=ma.auto_field()
    variante=ma.Nested(VarianteSchema)
    producto=ma.Nested(ProductoSchemaParaMaestroDetalle)
    
maestroDetalleSchema = MaestroDetalleSchema()
maestroDetallesSchema = MaestroDetalleSchema(many=True)
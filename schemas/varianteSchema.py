from config.marsh import ma
from models.variante import Variante

class VarianteSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Variante
    id=ma.auto_field()
    color=ma.auto_field()
    idProducto=ma.auto_field()
    
varianteSchema = VarianteSchema()
variantesSchema = VarianteSchema(many=True)



